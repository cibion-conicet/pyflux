'<ADbasic Header, Headerversion 001.001>
' Process_Number                 = 2
' Initial_Processdelay           = 3000
' Eventsource                    = Timer
' Control_long_Delays_for_Stop   = No
' Priority                       = High
' Version                        = 1
' ADbasic_Version                = 6.2.0
' Optimize                       = Yes
' Optimize_Level                 = 1
' Stacksize                      = 1000
' Info_Last_Save                 = PC-MINFLUX  PC-MINFLUX\USUARIO
'<Header End>
'process moveto: moveto_xyz by luciano a. masullo

'Parameters from 20 to 29 are used

'function to do a single (smooth) movement to desired position

'par_21: number of x pixels
'par_22: number of y pixels
'par_23: number of z pixels

'fpar23: setpoint x
'fpar24: setpoint y
'fpar25: setpoint z

'fpar_26: pixeltime

'fpar_70: keeps track of x position of the piezo
'fpar_71: keeps track of y position of the piezo
'fpar_72: keeps track of z position of the piezo

#INCLUDE .\data-acquisition.inc

dim currentx, currenty, currentz as float at dm_local
dim setpointx, setpointy, setpointz as float at dm_local
dim dx, dy, dz as float at dm_local
dim Nx,Ny,Nz,p as long at dm_local
dim time0, time1 as float at dm_local


INIT:
  
  time0 = 0
  time1 = 0

  currentx = fpar_70
  currenty = fpar_71
  currentz = fpar_72
  
  setpointx = fpar_23 
  setpointy = fpar_24
  setpointz = fpar_25
  
  if (setpointx > POSMAX) then setpointx = POSMAX 'check that set x position is not higher than POSMAX
  if (setpointx < POSMIN) then setpointx = POSMIN 'check that set x position is not lower than POSMIN
  
  if (setpointy > POSMAX) then setpointy = POSMAX 'check that set x position is not higher than POSMAX
  if (setpointy < POSMIN) then setpointy = POSMIN 'check that set x position is not lower than POSMIN
  
  if (setpointz > POSMAX) then setpointz = POSMAX 'check that set x position is not higher than POSMAX
  if (setpointz < POSMIN) then setpointz = POSMIN 'check that set x position is not lower than POSMIN
  
  Nx = par_21
  Ny = par_22
  Nz = par_23
 
  dx = (setpointx-currentx)/Nx
  dy = (setpointy-currenty)/Ny
  dz = (setpointz-currentz)/Nz

EVENT:

  time0 = Read_Timer() 
  DO 
    time1 = Read_Timer()
    
  UNTIL (Abs(time1 - time0) > fpar_26)
    
  currentx = currentx + dx
  currenty = currenty + dy
  currentz = currentz + dz
  
  if (currentx > POSMAX) then currentx = POSMAX 'check that set x position is not higher than POSMAX
  if (currentx < POSMIN) then currentx = POSMIN 'check that set x position is not lower than POSMIN
  
  if (currenty > POSMAX) then currenty = POSMAX 'check that set x position is not higher than POSMAX
  if (currenty < POSMIN) then currenty = POSMIN 'check that set x position is not lower than POSMIN
  
  if (currentz > POSMAX) then currentz = POSMAX 'check that set x position is not higher than POSMAX
  if (currentz < POSMIN) then currentz = POSMIN 'check that set x position is not lower than POSMIN

  DAC(1, currentx)
  DAC(2, currenty)
  DAC(6, currentz)
  
  fpar_70 = currentx
  fpar_71 = currenty
  fpar_72 = currentz
  
  p = 1 'error margin in ADwin units at which the moveTo is completed with currentpos = setpointpos
  
  if (((Abs(currentx - setpointx) < p) & (Abs(currenty - setpointy) < p)) & (Abs(currentz - setpointz) < p)) then
    
    time0 = Read_Timer() 
    DO 
      time1 = Read_Timer()
    
    UNTIL (Abs(time1 - time0) > fpar_26)
  
    currentx = setpointx
    currenty = setpointy
    currentz = setpointz
  
    if (currentx > POSMAX) then currentx = POSMAX 'check that set x position is not higher than POSMAX
    if (currentx < POSMIN) then currentx = POSMIN 'check that set x position is not lower than POSMIN
  
    if (currenty > POSMAX) then currenty = POSMAX 'check that set x position is not higher than POSMAX
    if (currenty < POSMIN) then currenty = POSMIN 'check that set x position is not lower than POSMIN
  
    if (currentz > POSMAX) then currentz = POSMAX 'check that set x position is not higher than POSMAX
    if (currentz < POSMIN) then currentz = POSMIN 'check that set x position is not lower than POSMIN

    DAC(1, currentx)
    DAC(2, currenty)
    DAC(6, currentz)
    
    fpar_70 = currentx
    fpar_71 = currenty
    fpar_72 = currentz
    
    End
   
  endif  
  

FINISH:
  

