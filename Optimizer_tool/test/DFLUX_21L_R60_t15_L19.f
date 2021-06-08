C
      SUBROUTINE DFLUX(FLUX,SOL,JSTEP,JINC,TIME,NOEL,NPT,COORDS,JLTYP,
     1 TEMP,PRESS,SNAME)
C
      INCLUDE 'ABA_PARAM.INC'
C
      DIMENSION COORDS(3),FLUX(2),TIME(2)
      CHARACTER*80 SNAME
C
C The total absorbed power needs to be calibrated
C with an intensity function QT  given by Goldak heat source model
C
C
      XX = COORDS(2)   
      YY = COORDS(3)   
      ZZ = COORDS(1)   
      TT = TIME(1)

C     .....
C	  .....
C     .....

      FLUX(1)    = QT 
      FLUX(2)=0.
      RETURN
      END
C
C