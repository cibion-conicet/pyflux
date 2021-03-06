'<ADbasic Header, Headerversion 001.001>
' Process_Number                 = 3
' Initial_Processdelay           = 3000
' Eventsource                    = Timer
' Control_long_Delays_for_Stop   = No
' Priority                       = Low
' Priority_Low_Level             = 1
' Version                        = 1
' ADbasic_Version                = 6.2.0
' Optimize                       = Yes
' Optimize_Level                 = 1
' Stacksize                      = 1000
' Info_Last_Save                 = PC-MINFLUX  PC-MINFLUX\USUARIO
'<Header End>
'process actuator_z: actuator_z by luciano a. masullo

'Parameters from 30 to 39 are used

'function to actuate in an ON/OFF z feedback loop.
'WARNING: the movement is not supposed to be smooth, therefore this script is to be used for small corrections ( < 200 nm)

'par_33 = number of pixels

'fpar_35 = setpoint z
'fpar_36: pixel time

'fpar_72 = currentz


#INCLUDE .\data-acquisition.inc

dim currentz as float at dm_local
dim setpointz as float at dm_local
dim flag as long at dm_local
dim time0, time1 as float at dm_local


INIT:
  
  time0 = 0
  time1 = 0
  
EVENT:
  
  'This loop holds the actuator until the flag is passed to start the actual function
  DO
    flag = par_30
  UNTIL (flag = 1)
 
  setpointz = fpar_32
  
  if (currentz > POSMAX) then currentz = POSMAX 'check that set x position is not higher than POSMAX
  if (currentz < POSMIN) then currentz = POSMIN 'check that set x position is not lower than POSMIN
  
  currentz = setpointz
  
  DAC(6, currentz)
  
  fpar_72 = currentz
  
  par_30 = 0
    
  time0 = Read_Timer() 
  DO 
    time1 = Read_Timer()
    
  UNTIL (Abs(time1 - time0) > fpar_36) 
  

FINISH:
  

