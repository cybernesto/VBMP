
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


SOURCE    EQU $4000

          JMP DEBUT

CALC      TXA            ; CALCUL ADRESSE LIGNE (X) HIRES
          AND #$C0
          STA MEM
          LSR
          LSR
          ORA MEM
          STA MEM
          TXA
          STA MEM+1
          ASL
          ASL
          ASL
          ROL MEM+1
          ASL
          ROL MEM+1
          ASL
          ROR MEM
          LDA MEM+1
          AND #$1F
          ORA #$20
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

SAVEDST   LDY DESTY
          LDX DESTX
          JSR CALC
          LDA BUFFDST
          LSR            ; DERNIER DECALLAGE POUR 7EMEBIT
          STA (MEM),Y
          INY
          CPY #40
          BNE S2
          DEX
          CPX #$FF
          BEQ FIN
          STX DESTX
          JSR READBMP    ; SAUTE 1 OCTET DANS BMP
          LDY #00
S2        STY DESTY
          LDA #06
          STA COMPTD
          RTS


DEBUT     BIT $C050
          BIT $C052
          BIT $C054
          BIT $C057

          SEC
          JSR $FE1F      ; TEST GS (THX A.V.)
          BCS GO1

          LDA $C036
          AND #$7F
          STA $C036      ; VITESSE LENTE
          LDA $C034      ;
          AND #$F0
          STA $C034      ; BORDURE NOIRE

GO1       LDA SOURCE+6
          SEC
          SBC #4
          CLC
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

FIN       PLA
          PLA
          STA $C010
BF        LDA $C000
          BPL BF
          STA $C010
          BIT $C051
          RTS
