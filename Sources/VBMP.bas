5  HOME 
10 D$ =  CHR$(4)
15  PRINT D$;"CAT"
20  PRINT "FILENAME TO DISPLAY (WITHOUT EXTENSION)"
25  INPUT F$: IF  LEN(F$) = 0 GOTO 25
30  PRINT D$;"BLOAD ";F$;".BMP,A$4000"
40  PRINT D$;"BRUN DISPLAY"
50 K =  PEEK( -16384)
60  IF K <127 GOTO 50
70  POKE  -16368,0
80  POKE  -16372,0: TEXT 
90  IF K < >128 +27 GOTO 5