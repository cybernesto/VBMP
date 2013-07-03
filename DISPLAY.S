***********************
* Apple II BMP Viewer *
* Arnaud Coqui}re     *
* Mario Patino        *
***********************

          LST OFF
          ORG $1000

MEM       EQU $06

COMPTS    EQU $18
COMPTD    EQU $19
SRCY      EQU $1A
DESTY     EQU $1B
DESTX     EQU $1C
BUFFBMP   EQU $1D
BUFFDST   EQU $1E
DHGR      EQU $1F


SOURCE    EQU $4000

          JMP DEBUT

CALC      TXA            ; CALCUL ADRESSE LIGNE (X) HIRES
          ASL
          TAY
          AND #$F0
          BPL C1
          ORA #$05
C1        BCC C2
          ORA #$0A
C2        ASL
          ASL
          STA MEM
          TYA
          AND #$0E
          ADC #$10
          ASL MEM
          ROL
          STA MEM+1
          RTS

READBMP   LDY SRCY
OFFSET    LDA SOURCE,Y
          STA BUFFBMP
          INY
          BNE S1
          INC OFFSET+2
S1        STY SRCY
          LDA #07
          STA COMPTS
          RTS

SAVEDST   LDX DESTX
          JSR CALC
          LDY DESTY
          LDA BUFFDST
          LSR            ; DERNIER DECALLAGE POUR 7EMEBIT
          STA (MEM),Y
          LDA DHGR
          BEQ HGR
          BIT $C01C
          BPL PAGE2
          BIT $C054
          JMP S2
PAGE2     BIT $C055
HGR       INY
          CPY #40
          BNE S2
          DEX
          CPX #$FF
          BEQ FIN
          STX DESTX
          JSR READBMP    ; SAUTE DES OCTETS DANS BMP
          LDA DHGR
          BEQ FILLD
          JSR READBMP
FILLD     LDY #00
S2        STY DESTY
          LDA #06
          STA COMPTD
          RTS
FIN       JMP END


DEBUT     BIT $C050      ; GRAPHIQUES
          BIT $C052      ; PLEIN G.
          BIT $C057      ; HAUTE RESOLUTION
          BIT $C054      ; PAGE1

          LDA #00
          STA DHGR
          LDA SOURCE+$12
          CMP #$18
          BEQ GSTEST

          STA $C00C
          BIT $C05E      ; DOUBLE HR
          STA $C05F
          STA $C05E
          STA $C05F
          STA $C00D
          STA $C05E
          CMP #$30
          BEQ MONO
          STA $C05F
          STA $C05E
          STA $C05F
          STA $C05E
MONO      STA $C001      ; SET80STORE
          BIT $C055      ; PAGE2
          LDA #01
          STA DHGR

GSTEST    SEC
          JSR $FE1F      ; TEST GS (THX A.V.)
          BCS GO1

          LDA $C036
          AND #$7F
          STA $C036      ; VITESSE LENTE
          LDA $C034      ;
          AND #$F0
          STA $C034      ; BORDURE NOIRE

GO1       LDA SOURCE+$0A
          ADC OFFSET+1
          STA OFFSET+1

          LDA #00
          STA BUFFDST
          STA SRCY
          STA DESTY
          LDX #191
          STX DESTX
          LDA #06
          STA COMPTD
          JSR READBMP

BP        ASL BUFFBMP
          ROR BUFFDST
          DEC COMPTS     ; 8 DECALLAGES
          BPL S3
          JSR READBMP
S3        DEC COMPTD     ; 7 ROTATIONS
          BPL S4
          JSR SAVEDST
S4        JMP BP

END       PLA
          PLA
          STA $C010
BF        LDA $C000
          BPL BF
          STA $C010
          STA $C000
          STA $C00C
          BIT $C053
          BIT $C054
          BIT $C051
          RTS
