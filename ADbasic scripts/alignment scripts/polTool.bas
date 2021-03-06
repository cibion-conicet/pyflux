'<ADbasic Header, Headerversion 001.001>
' Process_Number                 = 4
' Initial_Processdelay           = 3000
' Eventsource                    = Timer
' Control_long_Delays_for_Stop   = No
' Priority                       = High
' Version                        = 1
' ADbasic_Version                = 6.2.0
' Optimize                       = Yes
' Optimize_Level                 = 1
' Stacksize                      = 1000
' Info_Last_Save                 = USUARIO-PC  USUARIO-PC\USUARIO
'<Header End>
'process polarization tool: polTool by luciano a. masullo

'fpar_40: samplingtime
'fpar_41: signal readout

#INCLUDE .\data-acquisition.inc

dim time0, time1 as float at dm_local
dim fs, signal as float at dm_local


INIT:
  
  fs = fpar_40
  time0 = 0
  time1 = 0
  
EVENT:
  
  time0 = Read_Timer()
  
  DO
    time1 = Read_Timer()
    
  UNTIL (time1 - time0 > 1/fs)
  
  signal = ADC(3)
  fpar_41 = signal
  
FINISH:
  
  time1 = 0
  time0 = 0
  fpar_41 = 0
