﻿# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 13:41:48 2018

@authors: Luciano Masullo
"""

import numpy as np
import time
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from datetime import date, datetime
import os

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.ptime as ptime
import qdarkstyle # see https://stackoverflow.com/questions/48256772/dark-theme-for-in-qt-widgets

from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot

import sys
sys.path.append('C:\Program Files\Thorlabs\Scientific Imaging\ThorCam')
# install from https://instrumental-lib.readthedocs.io/en/stable/install.html
import tools.viewbox_tools as viewbox_tools
import tools.tools as tools
import tools.PSF as PSF
import tools.colormaps as cmaps
from scipy import optimize as opt

from instrumental.drivers.cameras import uc480
import scan
import drivers.ADwin as ADwin

DEBUG = True

def actuatorParameters(adwin, z_f, n_pixels_z=50, pixeltime=1000):

    z_f = tools.convert(z_f, 'XtoU')

    adwin.Set_Par(33, n_pixels_z)
    adwin.Set_FPar(35, z_f)
    adwin.Set_FPar(36, tools.timeToADwin(pixeltime))

def zMoveTo(adwin, z_f):

    actuatorParameters(adwin, z_f)
    adwin.Start_Process(3)

class Frontend(QtGui.QFrame):
    
    changedROI = pyqtSignal(np.ndarray)  # sends new roi size
    closeSignal = pyqtSignal()
    saveDataSignal = pyqtSignal(bool)
    
    paramSignal = pyqtSignal(dict)
    
    """
    Signals
        
    - changedROI:
        To: [backend] get_new_roi
        
    - closeSignal:
        To: [backend] stop
        
    - saveDataSignal:
        To: [backend] get_save_data_state
        
    - paramSignal:
        To: [backend] get_frontend_param

    """
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        
        self.roi = None
        self.cropped = False

        self.setup_gui()
        
    def emit_param(self):
        
        params = dict()
        params['pxSize'] = float(self.pxSizeEdit.text())
        
        self.paramSignal.emit(params)

    def roi_method(self):
        
        if self.cropped is True:  # code to go back to the (1280 x 1024) ROI
            
            x0 = 0
            y0 = 0
            x1 = 1280 
            y1 = 1024 
            
            value = np.array([x0, y0, x1, y1])
            self.changedROI.emit(value)
            self.cropped = False
        
        ROIpen = pg.mkPen(color='y')

        if self.roi is None:

            ROIpos = (0, 0)
            self.roi = viewbox_tools.ROI(300, self.vb, ROIpos,
                                         handlePos=(1, 0),
                                         handleCenter=(0, 1),
                                         scaleSnap=True,
                                         translateSnap=True,
                                         pen=ROIpen)

        else:

            self.vb.removeItem(self.roi)
            self.roi.hide()

            ROIpos = (0, 0)
            self.roi = viewbox_tools.ROI(300, self.vb, ROIpos,
                                         handlePos=(1, 0),
                                         handleCenter=(0, 1),
                                         scaleSnap=True,
                                         translateSnap=True,
                                         pen=ROIpen)
        
        self.selectROIbutton.setEnabled(True)
        
    def select_roi(self):
        
        self.cropped = True
        self.getStats = True
    
        ROIpos = np.array(self.roi.pos())
        roisize = np.array(self.roi.size())
        
        y0 = int(ROIpos[0])
        x0 = int(ROIpos[1])
        y1 = int(ROIpos[0] + roisize[0])
        x1 = int(ROIpos[1] + roisize[1])
        
        value = np.array([x0, y0, x1, y1])
        
        if (value[0] < 0) or (value[1] < 0) or (value[2] > 1280) or (value[3] > 1024):
            print(datetime.now(), '[focus] ROI cannot be set as outside of camera FOV')
            x0 = 0
            y0 = 0
            x1 = 1280 
            y1 = 1024 
            value = np.array([x0, y0, x1, y1])
            
        self.changedROI.emit(value)
    
        self.vb.removeItem(self.roi)
        self.roi.hide()
        self.roi = None
        
        self.selectROIbutton.setEnabled(False)
        self.deleteROIbutton.setEnabled(True)
        self.vb.enableAutoRange()
        
#    def toggleFocus(self):
#        
#        if self.lockButton.isChecked():
#            
#            self.lockFocusSignal.emit(True)
#
##            self.setpointLine = self.focusGraph.zPlot.addLine(y=self.setPoint, pen='r')
#            
#        else:
#            
#            self.lockFocusSignal.emit(False)
        
    def delete_roi(self):
        
        self.vb.removeItem(self.roi)
        x0 = 0
        y0 = 0
        x1 = 1280 
        y1 = 1024 
            
        value = np.array([x0, y0, x1, y1])
        self.changedROI.emit(value)
        self.cropped = False
        
        self.roi = None
        
        print(datetime.now(), '[focus] ROI deleted')
        
        self.deleteROIbutton.setEnabled(False)
            
    @pyqtSlot(bool)        
    def toggle_liveview(self, on):
        if on:
            self.liveviewButton.setChecked(True)
            print(datetime.now(), '[focus] focus live view started')
        else:
            self.liveviewButton.setChecked(False)
            try:
                self.roi.hide()
            except:
                pass
            self.img.setImage(np.zeros((512,512)), autoLevels=False)
            print(datetime.now(), '[focus] focus live view stopped')
            
    def emit_save_data_state(self):
        
        if self.saveDataBox.isChecked():
            
            self.saveDataSignal.emit(True)
            
        else:
            
            self.saveDataSignal.emit(False)
            
#    def toggle_stats(self):
#        
#        if self.feedbackLoopBox.isChecked():
#        
#            self.focusMean = self.focusGraph.plot.addLine(y=self.setPoint,
#                                                          pen='c')
#        
#        else:
#            
#            self.focusGraph.removeItem(self.focusMean)
        
    @pyqtSlot(np.ndarray)
    def get_image(self, img):
        
        #  The croppingis done because otherwise the displayed image will be
        #  300 x 1024. It doesn't affect the performance of the system
        
        if self.cropped is False: 
            
            self.img.setImage(img, autoLevels=False)
        
        else:

            croppedimg = img[0:300, 0:300]
            self.img.setImage(croppedimg)
            
    @pyqtSlot(np.ndarray, np.ndarray)
    def get_data(self, time, position):
        
        self.focusCurve.setData(time, position)
             
        if self.feedbackLoopBox.isChecked():
            
            if len(position) > 2:
        
                zMean = np.mean(position)
                zStDev = np.std(position)
                
                # TO DO: fix focus stats
                
#                self.focusMean.setValue(zMean)
#                self.focusStDev0.setValue(zMean - zStDev)
#                self.focusStDev1.setValue(zMean + zStDev)
      
    @pyqtSlot(float)          
    def get_setpoint(self, value):
        
        self.setPoint = value
        
        print('[focus] set point', value)
        
        # TO DO: fix setpoint line
        
#        self.focusSetPoint = self.focusGraph.zPlot.addLine(y=self.setPoint,
#                                                           pen=pg.mkPen('r', width=2))
#        self.focusMean = self.focusGraph.zPlot.addLine(y=self.setPoint,
#                                                       pen='c')
#        self.focusStDev0 = self.focusGraph.zPlot.addLine(y=self.setPoint,
#                                                         pen='c')
#        
#        self.focusStDev1 = self.focusGraph.zPlot.addLine(y=self.setPoint,
#                                                         pen='c')
        
    def clear_graph(self):
        
        # TO DO: fix setpoint line
        
#        self.focusGraph.zPlot.removeItem(self.focusSetPoint)
#        self.focusGraph.zPlot.removeItem(self.focusMean)
#        self.focusGraph.zPlot.removeItem(self.focusStDev0)
#        self.focusGraph.zPlot.removeItem(self.focusStDev1)
        
        pass
    
    @pyqtSlot(int, bool)    
    def update_shutter(self, num, on):
        
        '''
        setting of num-value:
            0 - signal send by scan-gui-button --> change state of all minflux shutters
            1...6 - shutter 1-6 will be set according to on-variable, i.e. either true or false; only 1-4 controlled from here
            7 - set all minflux shutters according to on-variable
            8 - set all shutters according to on-variable
        for handling of shutters 1-5 see [scan] and [focus]
        '''
        
        if (num == 5)  or (num == 8):
            self.shutterCheckbox.setChecked(on)
            
    def make_connection(self, backend):
            
        backend.changedImage.connect(self.get_image)
        backend.changedData.connect(self.get_data)
        backend.changedSetPoint.connect(self.get_setpoint)
        backend.shuttermodeSignal.connect(self.update_shutter)
        backend.liveviewSignal.connect(self.toggle_liveview)


    def setup_gui(self):
        
         # Focus lock widget
         
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.setMinimumSize(2, 200)
        
        # LiveView Button

        self.liveviewButton = QtGui.QPushButton('Camera LIVEVIEW')
        self.liveviewButton.setCheckable(True)

        # turn ON/OFF feedback loop
        
        self.feedbackLoopBox = QtGui.QCheckBox('Feedback loop')
        
        #shutter button and label
        self.shutterLabel = QtGui.QLabel('Shutter open?')
        self.shutterCheckbox = QtGui.QCheckBox('IR laser')
        
        # ROI button

        self.ROIbutton = QtGui.QPushButton('ROI')
        self.selectROIbutton = QtGui.QPushButton('Select ROI')
        self.deleteROIbutton = QtGui.QPushButton('Delete ROI')
        self.calibrationButton = QtGui.QPushButton('Calibrate')
        
        self.exportDataButton = QtGui.QPushButton('Export data')
        self.saveDataBox = QtGui.QCheckBox("Save data")
        self.clearDataButton = QtGui.QPushButton('Clear data')
        
        self.pxSizeLabel = QtGui.QLabel('Pixel size (nm)')
        self.pxSizeEdit = QtGui.QLineEdit('10')
        self.focusPropertiesDisplay = QtGui.QLabel(' st_dev = 0  max_dev = 0')
        
        self.deleteROIbutton.setEnabled(False)
        self.selectROIbutton.setEnabled(False)

        
        # gui connections
        
        self.saveDataBox.stateChanged.connect(self.emit_save_data_state)
        self.selectROIbutton.clicked.connect(self.select_roi)
        self.clearDataButton.clicked.connect(self.clear_graph)
        self.pxSizeEdit.textChanged.connect(self.emit_param)
        self.deleteROIbutton.clicked.connect(self.delete_roi)
        self.ROIbutton.clicked.connect(self.roi_method)

        # focus camera display
        
        self.camDisplay = pg.GraphicsLayoutWidget()
        self.camDisplay.setMinimumHeight(200)
        self.camDisplay.setMinimumWidth(200)
        
        self.vb = self.camDisplay.addViewBox(row=0, col=0)
        self.vb.setAspectLocked(True)
        self.vb.setMouseMode(pg.ViewBox.RectMode)
        self.img = pg.ImageItem()
        self.img.translate(-0.5, -0.5)
        self.vb.addItem(self.img)

        self.hist = pg.HistogramLUTItem(image=self.img)   # set up histogram for the liveview image
        lut = viewbox_tools.generatePgColormap(cmaps.inferno)
        self.hist.gradient.setColorMap(lut)
        self.hist.vb.setLimits(yMin=0, yMax=10000)

        for tick in self.hist.gradient.ticks:
            tick.hide()
            
        self.camDisplay.addItem(self.hist, row=0, col=1)
        
        # focus lock graph
        
        self.focusGraph = pg.GraphicsWindow()
        self.focusGraph.setAntialiasing(True)
        
        self.focusGraph.statistics = pg.LabelItem(justify='right')
        self.focusGraph.addItem(self.focusGraph.statistics, row=0, col=0)
        self.focusGraph.statistics.setText('---')
        
        self.focusGraph.zPlot = self.focusGraph.addPlot(row=0, col=0)
        self.focusGraph.zPlot.setLabels(bottom=('Time', 's'),
                                        left=('CM x position', 'px'))
        self.focusGraph.zPlot.showGrid(x=True, y=True)
        self.focusCurve = self.focusGraph.zPlot.plot(pen='y')
 
#        self.focusSetPoint = self.focusGraph.plot.addLine(y=self.setPoint, pen='r')

        # GUI layout
        
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        
        # parameters widget
        
        self.paramWidget = QtGui.QFrame()
        self.paramWidget.setFrameStyle(QtGui.QFrame.Panel |
                                       QtGui.QFrame.Raised)
        
        self.paramWidget.setFixedHeight(330)
        self.paramWidget.setFixedWidth(140)
        
        subgrid = QtGui.QGridLayout()
        self.paramWidget.setLayout(subgrid)
        
        subgrid.addWidget(self.calibrationButton, 7, 0, 1, 2)
        subgrid.addWidget(self.exportDataButton, 5, 0, 1, 2)
        subgrid.addWidget(self.clearDataButton, 6, 0, 1, 2)
        
        subgrid.addWidget(self.pxSizeLabel, 8, 0)
        subgrid.addWidget(self.pxSizeEdit, 8, 1)
        
        subgrid.addWidget(self.feedbackLoopBox, 9, 0)
        subgrid.addWidget(self.saveDataBox, 10, 0)
        
        subgrid.addWidget(self.liveviewButton, 1, 0, 1, 2)
        subgrid.addWidget(self.ROIbutton, 2, 0, 1, 2)
        subgrid.addWidget(self.selectROIbutton, 3, 0, 1, 2)
        subgrid.addWidget(self.deleteROIbutton, 4, 0, 1, 2)
        
        subgrid.addWidget(self.shutterLabel, 11, 0)
        subgrid.addWidget(self.shutterCheckbox, 12, 0)
        
        grid.addWidget(self.paramWidget, 0, 0)
        grid.addWidget(self.focusGraph, 0, 1)
        grid.addWidget(self.camDisplay, 0, 2)
        
        #didnt want to work when being put at earlier point in this function
        self.liveviewButton.clicked.connect(lambda: self.toggle_liveview(self.liveviewButton.isChecked()))

    def closeEvent(self, *args, **kwargs):
        
        self.closeSignal.emit()
        time.sleep(1)
        
        focusThread.exit()
        super().closeEvent(*args, **kwargs)
        app.quit()
        
        
class Backend(QtCore.QObject):
    
    changedImage = pyqtSignal(np.ndarray)
    changedData = pyqtSignal(np.ndarray, np.ndarray)
    changedSetPoint = pyqtSignal(float)
    
    zIsDone = pyqtSignal(bool, float)
    shuttermodeSignal = pyqtSignal(int, bool)
    liveviewSignal = pyqtSignal(bool)
    focuslockpositionSignal = pyqtSignal(float)

    """
    Signals
    
    - changedImage:
        To: [frontend] get_image
             
    - changedData:
        To: [frontend] get_data
        
    - changedSetPoint:
        To: [frontend] get_setpoint
        
    - zIsDone:
        To: [psf] get_z_is_done
        
    - shuttermodeSignal:
        To: [frontend] update_shutter
        
    - focuslockpositionSignal:
        To: [scan] get current focus lock position
        
    """

    def __init__(self, camera, adw, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.camera = camera
        self.adw = adw
        self.feedback_active = False
        self.cropped = False
        self.standAlone = False
        self.camON = False
        self.roi_area = np.zeros(4)
        
        today = str(date.today()).replace('-', '') # TO DO: change to get folder from microscope
        root = r'C:\\Data\\'
        folder = root + today
        
        filename = r'zdata.txt'
        self.filename = os.path.join(folder, filename)
        
        self.save_data_state = False
    
        self.npoints = 400
        
        # checks image size
        
        rawimage = self.camera.latest_frame()
        image = np.sum(rawimage, axis=2)
        
        self.pxSize = 10   # in nm, TO DO: change for an input from the user
        
        self.sensorSize = np.array(image.shape)
        self.focusSignal = 0
        
        # set focus update rate
        
        self.scansPerS = 20

        self.focusTime = 1000 / self.scansPerS
        self.focusTimer = QtCore.QTimer()
        
        self.reset()
        self.reset_data_arrays()
        
    @pyqtSlot(dict)
    def get_frontend_param(self, params):
        
        self.pxSize = params['pxSize']
        
        print(datetime.now(), ' [focus] got px size', self.pxSize, ' nm')
        
    def set_actuator_param(self, pixeltime=1000):

        self.adw.Set_FPar(36, tools.timeToADwin(pixeltime))
        
        # set-up actuator initial param
    
        z_f = tools.convert(10, 'XtoU') # TO DO: make this more robust
        
        self.adw.Set_FPar(32, z_f)

        self.adw.Set_Par(30, 1)
        
    def actuator_z(self, z_f):
        
        z_f = tools.convert(z_f, 'XtoU')
          
        self.adw.Set_FPar(32, z_f)
        
        self.adw.Set_Par(30, 1)
    
    @pyqtSlot(bool)
    def liveview(self, value):

        if value:
            self.camON = True
            self.liveview_start()

        else:
            self.liveview_stop()
            self.camON = False

        
    def liveview_start(self):
        
        if self.camON:
            self.camera.stop_live_video()
            self.camON = False
        
        self.camON = True
        self.camera.start_live_video(framerate='20 Hz')

        self.focusTimer.start(self.focusTime)
        
    def liveview_stop(self):
        
        self.focusTimer.stop()
        self.camON = False
        
        x0 = 0
        y0 = 0
        x1 = 1280 
        y1 = 1024 
            
        val = np.array([x0, y0, x1, y1])
        self.get_new_roi(val)
                
    @pyqtSlot(int, bool)
    def toggle_ir_shutter(self, num, val):
        
        #TODO: change code to also update checkboxes in case of minflux measurement
        if (num == 5) or (num == 8):
            if val:
                tools.toggle_shutter(self.adw, 5, True)
                print(datetime.now(), '[focus] IR shutter opened')
            else:
                tools.toggle_shutter(self.adw, 5, False)
                print(datetime.now(), '[focus] IR shutter closed')
                
    @pyqtSlot(int, bool)
    def shutter_handler(self, num, on):
        self.shuttermodeSignal.emit(num, on)
        
    @pyqtSlot(bool)
    def toggle_tracking(self, val):
        
        '''
        Connection: [frontend] trackingBeadsBox.stateChanged
        Description: toggles ON/OFF tracking of IR reflection from sample. 
        Drift correction feedback loop is not automatically started.
        
        '''

        #TODO: write track procedure like in xy-tracking
        self.startTime = time.time()
        
        if val is True:
            
            self.reset()
            self.reset_data_arrays()
            
            self.tracking_value = True
                    
        if val is False:
        
            self.tracking_value = False
            
        
    @pyqtSlot(bool)
    def toggle_feedback(self, val, mode='continous'):
        ''' Toggles ON/OFF feedback for either continous (TCSPC) 
        or discrete (scan imaging) correction'''
        
        if val is True:
            
            self.reset()
            self.setup_feedback()
            self.update()
            self.feedback_active = True
            
            # set up and start actuator process
            
            if mode == 'continous':
            
                self.set_actuator_param()
                self.adw.Start_Process(3)
                print(datetime.now(), '[focus] Process 3 started')
            
            print(datetime.now(), ' [focus] Feedback loop ON')
            
        if val is False:
            
            self.feedback_active = False
            print(datetime.now(), ' [focus] Feedback loop OFF')
            
            if mode == 'continous':
            
                self.adw.Stop_Process(3)
                print(datetime.now(), '[focus] Process 3 stopped')

    
    @pyqtSlot()    
    def setup_feedback(self):
        
        ''' set up on/off feedback loop'''
        
        print(datetime.now(), '[focus] feedback setup 0')

        self.setPoint = self.focusSignal * self.pxSize # define setpoint
        initial_z = tools.convert(self.adw.Get_FPar(72), 'UtoX') # current z position of the piezo
        self.target_z = initial_z # set initial_z as target_z
        
        self.changedSetPoint.emit(self.focusSignal)
        
        print(datetime.now(), '[focus] feedback setup 1')

        # TO DO: implement calibrated version of this
    
    def update_feedback(self, mode='continous'):
        
        dz = self.focusSignal * self.pxSize - self.setPoint

#        print('dz', dz, ' nm')
        
        threshold = 7 # in nm
        far_threshold = 20 # in nm
        correct_factor = 1
        security_thr = 200 # in nm
        
        if np.abs(dz) > threshold:
            
            if np.abs(dz) < far_threshold:
                
                dz = correct_factor * dz
    
        if np.abs(dz) > security_thr:
            
            print(datetime.now(), '[focus] Correction movement larger than 200 nm, active correction turned OFF')
            
        else:
            
            self.target_z = self.target_z + dz/1000  # conversion to µm
            
            if mode == 'continous':
                
                self.actuator_z(self.target_z)
                
            if mode == 'discrete':
                
                pass  # it's enough to have saved the value self.target_z
                
                print(datetime.now(), '[focus] discrete correction to', self.target_z)
            
    def update_graph_data(self):
        
        ''' update of the data displayed in the gui graph '''

        if self.ptr < self.npoints:
            self.data[self.ptr] = self.focusSignal
            self.time[self.ptr] = self.currentTime
            
            self.changedData.emit(self.time[0:self.ptr + 1],
                                  self.data[0:self.ptr + 1])

        else:
            self.data[:-1] = self.data[1:]
            self.data[-1] = self.focusSignal
            self.time[:-1] = self.time[1:]
            self.time[-1] = self.currentTime

            self.changedData.emit(self.time, self.data)

        self.ptr += 1
            
    def update_stats(self):
        
        # TO DO: fix this function

        signal = self.focusSignal

        if self.n == 1:
            self.mean = signal
            self.mean2 = self.mean**2
        else:
            self.mean += (signal - self.mean)/self.n
            self.mean2 += (signal**2 - self.mean2)/self.n

        # Stats
        self.std = np.sqrt(self.mean2 - self.mean**2)
        self.max_dev = np.max([self.max_dev,
                              self.focusSignal - self.setPoint])
        statData = 'std = {}    max_dev = {}'.format(np.round(self.std, 3),
                                                     np.round(self.max_dev, 3))
        self.gui.focusGraph.statistics.setText(statData)

        self.n += 1
        
    def update(self):
        
        self.acquire_data()
        self.update_graph_data()
        
        #  if locked, correct position
        
        if self.feedback_active:
            
#            self.updateStats()
            self.update_feedback()
            
        if self.save_data_state:
                        
            self.time_array.append(self.currentTime)
            self.z_array.append(self.focusSignal)
            
    def acquire_data(self):
        
        # acquire image
    
        raw_image = self.camera.latest_frame()
        image = np.sum(raw_image, axis=2)   # sum the R, G, B images

        # send image to gui

        self.changedImage.emit(image)
                
        argmax = np.unravel_index(np.argmax(image, axis=None), image.shape)
        
        roisize = self.roi_area[2] - self.roi_area[0]
        if roisize == 300:
            extent = 148 # subroi extent in px
            argmax[0] = 150 
        else:
            extent = 300
        
        # get mass center
        self.massCenter = np.array(ndi.measurements.center_of_mass(image[argmax[0]-extent:argmax[0]+extent, argmax[1]-extent:argmax[1]+extent]))
        print(self.massCenter[0], argmax[1], self.roi_area, image.shape)
        self.focusSignal = argmax[0] - extent + self.massCenter[0] + self.roi_area[0]
        self.currentTime = ptime.time() - self.startTime
        
    @pyqtSlot(bool, bool)
    def single_z_correction(self, feedback_val, initial):
        
        if initial:
        
            if self.camON:
                self.focusTimer.stop()
                self.camera.stop_live_video()            
            
            #self.liveviewSignal.emit(True)
            self.reset()
            self.reset_data_arrays()
            self.camON = True
            time.sleep(0.200)
            self.camera.start_live_video(framerate='20 Hz')
            
            time.sleep(0.100)
            
            self.get_new_roi(self.roi_area)
        
            time.sleep(0.200)
        
        self.acquire_data()
        self.update_graph_data()
                
        if initial:
            
            self.setup_feedback()
            
        else:
        
            self.update_feedback(mode='discrete')
        
        if self.save_data_state:
            
            self.time_array.append(self.currentTime)
            self.z_array.append(self.focusSignal)
                    
        self.zIsDone.emit(True, self.target_z)

    def calibrate(self):
        
        # TO DO: fix calibration function
        
        self.focusTimer.stop()
        time.sleep(0.100)
        
        nsteps = 40
        xmin = 9.5  # in µm
        xmax = 10.5   # in µm
        xrange = xmax - xmin  
        
        calibData = np.zeros(40)
        xData = np.arange(xmin, xmax, xrange/nsteps)
        
        zMoveTo(self.actuator, xmin)
        
        time.sleep(0.100)
        
        for i in range(nsteps):
            
            zMoveTo(self.actuator, xmin + (i * 1/nsteps) * xrange)
            self.update()
            calibData[i] = self.focusSignal
            
        plt.plot(xData, calibData, 'o')
            
        time.sleep(0.200)
        
        self.focusTimer.start(self.focusTime)
    
            
    def reset(self):
        
        self.data = np.zeros(self.npoints)
        self.time = np.zeros(self.npoints)
        self.ptr = 0
        self.startTime = ptime.time()

        self.max_dev = 0
        self.mean = self.focusSignal
        self.std = 0
        self.n = 1
        
    def reset_data_arrays(self):
        
        self.time_array = []
        self.z_array = []
        
    def export_data(self):
        
        fname = self.filename
        #case distinction to prevent wrong filenaming when starting minflux or psf measurement
        if fname[0] == '!':
            filename = fname[1:]
        else:
            filename = tools.getUniqueName(fname)
        filename = filename + '_zdata.txt'

        size = np.size(self.z_array)
        savedData = np.zeros((2, size))

        savedData[0, :] = np.array(self.time_array)
        savedData[1, :] = np.array(self.z_array)
        
        np.savetxt(filename, savedData.T, header='t (s), z (px)')
        
        print(datetime.now(), '[focus] z data exported to', filename)
        
    @pyqtSlot()    
    def get_stop_signal(self):
        
        """
        From: [psf]
        Description: stops liveview, tracking, feedback if they where running to
        start the psf measurement with discrete xy - z corrections
        """
            
        self.toggle_feedback(False)
        self.toggle_tracking(False)
        
        self.save_data_state = True  # TO DO: sync this with GUI checkboxes (Lantz typedfeat?)
            
        self.reset()
        self.reset_data_arrays()
        
        
    @pyqtSlot()    
    def get_lock_signal(self):
        
        if not self.camON:
            self.liveviewSignal.emit(True)
            
        self.reset_data_arrays()
        
        self.toggle_feedback(True)
        self.toggle_tracking(True)
        self.save_data_state = True
        
        # TO DO: fix updateGUIcheckboxSignal    
        
#        self.updateGUIcheckboxSignal.emit(self.tracking_value, 
#                                          self.feedback_active, 
#                                          self.save_data_state)
        
        print(datetime.now(), '[focus] System focus locked')
            
    @pyqtSlot(np.ndarray)
    def get_new_roi(self, val):
        
        
        self.roi_area = val
        
        if (val[0] < 0) or (val[1] < 0) or (val[2] > 1280) or (val[3] > 1024):
            print(datetime.now(), '[focus] ROI cannot be set as outside camera FOV')
            x0 = 0
            y0 = 0
            x1 = 1280 
            y1 = 1024 
            self.roi_area = np.array([x0, y0, x1, y1])
            
        self.camera._set_AOI(*self.roi_area)
        
        if DEBUG:
            print(datetime.now(), '[focus] ROI changed to', self.camera._get_AOI())
    
    @pyqtSlot(bool, str)   
    def get_tcspc_signal(self, val, fname):
        
        """ 
        Get signal to start/stop xy position tracking and lock during 
        tcspc acquisition. It also gets the name of the tcspc file to produce
        the corresponding xy_data file
        
        bool val
        True: starts the tracking and feedback loop
        False: stops saving the data and exports the data during tcspc measurement
        tracking and feedback are not stopped automatically 
        
        """
        
        self.filename = fname
         
        if val is True:
            
            self.reset()
            self.reset_data_arrays()
            
            self.save_data_state = True
            self.toggle_feedback(True)
            self.save_data_state = True
            
        else:
            
            self.export_data()
            self.save_data_state = False
            
        # TO DO: fix updateGUIcheckboxSignal    
        
#        self.updateGUIcheckboxSignal.emit(self.tracking_value, 
#                                          self.feedback_active, 
#                                          self.save_data_state)
            
    @pyqtSlot(bool, str)   
    def get_scan_signal(self, val, fname):
        
        """ 
        Get signal to stop continous xy tracking/feedback if active and to
        go to discrete xy tracking/feedback mode if required
        """
        
    @pyqtSlot(bool)
    def get_save_data_state(self, val):
        
        self.save_data_state = val
        
    @pyqtSlot(str)    
    def get_end_measurement_signal(self, fname):
        
        """ 
        From: [minflux] or [psf]
        Description: at the end of the measurement exports the xy data

        """ 
        
        self.filename = fname
        self.export_data()
        
        self.toggle_feedback(False)
        self.toggle_tracking(False)
        
        if self.camON:
            self.focusTimer.stop()
            self.liveviewSignal.emit(False)
        
    def set_moveTo_param(self, x_f, y_f, z_f, n_pixels_x=128, n_pixels_y=128,
                         n_pixels_z=128, pixeltime=2000):

        x_f = tools.convert(x_f, 'XtoU')
        y_f = tools.convert(y_f, 'XtoU')
        z_f = tools.convert(z_f, 'XtoU')

        self.adw.Set_Par(21, n_pixels_x)
        self.adw.Set_Par(22, n_pixels_y)
        self.adw.Set_Par(23, n_pixels_z)

        self.adw.Set_FPar(23, x_f)
        self.adw.Set_FPar(24, y_f)
        self.adw.Set_FPar(25, z_f)

        self.adw.Set_FPar(26, tools.timeToADwin(pixeltime))

    def moveTo(self, x_f, y_f, z_f, pixeltime=2000):

        self.set_moveTo_param(x_f, y_f, z_f, pixeltime)
        self.adw.Start_Process(2)
        
        
    def gaussian_fit(self):
        
        # set main reference frame
        
        ymin, xmin, ymax, xmax = self.roi_area
        ymin_nm, xmin_nm, ymax_nm, xmax_nm = self.roi_area * self.pxSize
        
        # select the data of the image corresponding to the ROI

        array = self.image #[xmin:xmax, ymin:ymax]
        
        # set new reference frame
        
        xrange_nm = xmax_nm - xmin_nm
        yrange_nm = ymax_nm - ymin_nm
             
        x_nm = np.arange(0, xrange_nm, self.pxSize)
        y_nm = np.arange(0, yrange_nm, self.pxSize)
        
        (Mx_nm, My_nm) = np.meshgrid(x_nm, y_nm)
        
        # find max 
        
        argmax = np.unravel_index(np.argmax(array, axis=None), array.shape)
        
        x_center_id = argmax[0]
        y_center_id = argmax[1]
        
        # define area around maximum
    
        xrange = 10 # in px
        yrange = 10 # in px
        
        xmin_id = int(x_center_id-xrange)
        xmax_id = int(x_center_id+xrange)
        
        ymin_id = int(y_center_id-yrange)
        ymax_id = int(y_center_id+yrange)
        
        array_sub = array[xmin_id:xmax_id, ymin_id:ymax_id]
                
        xsubsize = 2 * xrange
        ysubsize = 2 * yrange
        
#        plt.imshow(array_sub, cmap=cmaps.parula, interpolation='None')
        
        x_sub_nm = np.arange(0, xsubsize) * self.pxSize
        y_sub_nm = np.arange(0, ysubsize) * self.pxSize

        [Mx_sub, My_sub] = np.meshgrid(x_sub_nm, y_sub_nm)
        
        # make initial guess for parameters
        
        bkg = np.min(array)
        A = np.max(array) - bkg
        σ = 400 # nm
        x0 = x_sub_nm[int(xsubsize/2)]
        y0 = y_sub_nm[int(ysubsize/2)]
        
        initial_guess_G = [A, x0, y0, σ, σ, bkg]
         
        poptG, pcovG = opt.curve_fit(PSF.gaussian2D, (Mx_sub, My_sub), 
                                     array_sub.ravel(), p0=initial_guess_G)
        
        # retrieve results

        poptG = np.around(poptG, 2)
    
        A, x0, y0, σ_x, σ_y, bkg = poptG
        
        print(poptG)
        
#        x = x0 + Mx_nm[xmin_id, ymin_id]
#        y = y0 + My_nm[xmin_id, ymin_id]
#        
##        self.currentx = x
##        self.currenty = y
#        
#        # if to avoid (probably) false localizations
#        
#        maxdist = 200 # in nm
#        
#        if self.initial is False:
#        
#            if np.abs(x - self.currentx) < maxdist and np.abs(y - self.currenty) < maxdist:
#        
#                self.currentx = x
#                self.currenty = y
#                
##                print(datetime.now(), '[xy_tracking] normal')
#                
#            else:
#                
#                pass
#                
#                print(datetime.now(), '[xy_tracking] max dist exceeded')
#        
#        else:
#            
#            self.currentx = x
#            self.currenty = y
            
#            print(datetime.now(), '[xy_tracking] else')
       
        print(x0, y0)
        
    @pyqtSlot(float)
    def get_focuslockposition(self, position):
        self.focuslockpositionSignal.emit(self.focusSignal)
        
    @pyqtSlot()
    def stop(self):
        
        self.toggle_ir_shutter(8, False)
        time.sleep(1)
        
        self.focusTimer.stop()
        
        #prevent system to throw weird errors when not being able to close the camera, see uc480.py --> close()
#        try:
        self.reset()
#        except:
#            pass
        
        if self.standAlone is True:
            
            # Go back to 0 position
    
            x_0 = 0
            y_0 = 0
            z_0 = 0
    
            self.moveTo(x_0, y_0, z_0)
            
        self.camera.close()

        print(datetime.now(), '[focus] Focus stopped')
        
        # clean up aux files from NiceLib
        
        try:
            os.remove(r'C:\Users\USUARIO\Documents\GitHub\pyflux\lextab.py')
            os.remove(r'C:\Users\USUARIO\Documents\GitHub\pyflux\yacctab.py')
        except:
            pass
        
        
    def make_connection(self, frontend):
          
        frontend.changedROI.connect(self.get_new_roi)
        frontend.closeSignal.connect(self.stop)
#        frontend.lockFocusSignal.connect(self.lock_focus)
#        frontend.feedbackLoopBox.stateChanged.connect(lambda: self.toggle_feedback(frontend.feedbackLoopBox.isChecked()))
        frontend.saveDataSignal.connect(self.get_save_data_state)
        frontend.exportDataButton.clicked.connect(self.export_data)
        frontend.clearDataButton.clicked.connect(self.reset)
        frontend.clearDataButton.clicked.connect(self.reset_data_arrays)
        frontend.calibrationButton.clicked.connect(self.calibrate)
        frontend.shutterCheckbox.stateChanged.connect(lambda: self.toggle_ir_shutter(8, frontend.shutterCheckbox.isChecked()))

        frontend.paramSignal.connect(self.get_frontend_param)
        frontend.liveviewButton.clicked.connect(self.liveview)


if __name__ == '__main__':
    
    if not QtGui.QApplication.instance():
        app = QtGui.QApplication([])
    else:
        app = QtGui.QApplication.instance()
        
    #app.setStyle(QtGui.QStyleFactory.create('fusion'))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    
    print(datetime.now(), '[focus] Focus lock module running in stand-alone mode')
    
    # initialize devices
    
    DEVICENUMBER = 0x1
    adw = ADwin.ADwin(DEVICENUMBER, 1)
    scan.setupDevice(adw)
    
    #if camera wasnt closed properly just keep using it without opening new one
    try:
        cam = uc480.UC480_Camera()
    except:
        pass
    
    gui = Frontend()   
    worker = Backend(cam, adw)
    worker.standAlone = True
    
    worker.make_connection(gui)
    gui.make_connection(worker)
    
    gui.emit_param()
    
    focusThread = QtCore.QThread()
    worker.moveToThread(focusThread)
    worker.focusTimer.moveToThread(focusThread)
    worker.focusTimer.timeout.connect(worker.update)
    
    focusThread.start()
    
    # initialize fpar_70, fpar_71, fpar_72 ADwin position parameters
        
    pos_zero = tools.convert(0, 'XtoU')
        
    worker.adw.Set_FPar(70, pos_zero)
    worker.adw.Set_FPar(71, pos_zero)
    worker.adw.Set_FPar(72, pos_zero)
    
    #worker.moveTo(10, 10, 10) # in µm
    #Very strange problem when using 
    
    gui.setWindowTitle('Focus lock')
    gui.resize(1500, 500)

    gui.show()
    #app.exec_()
        