import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import pyqtgraph as pg
from PyQt5.QtWidgets import QFileDialog
from numpy import linspace
from pyqtgraph import PlotWidget, plot
from math import *
from numpy import linspace, cos, sin, pi, ceil, floor, arange


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("sample.ui", self)
        self.Upload.clicked.connect(self.open)
        self.Plotdata.clicked.connect(self.plot)
        self.graph1.setBackground('black')
        self.graph2.setBackground('black')
        self.SamplingPoints.clicked.connect(self.plotSamples)
        self.ShowSampledGraph.clicked.connect(self.plotSeparateSamples)
        self.clearSample.clicked.connect(self.clear)
        self.show()
        self.horizontalSlider.setMaximum(80)

    def open(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '', 'All Files (*.*)')
        if path != ('', ''):
            print("File path : " + path[0])

    def plot(self):
        # sampling a signal badlimited to 40 Hz
        # with a sampling rate of 800 Hz
        f = 40;  # Hz
        tmin = -1
        tmax = 1
        t = linspace(tmin, tmax, 900)
        x = cos(2 * pi * t) + cos(2 * pi * f * t)  # signal sampling
        self.graph1.plot(t, x, pen='black')

    def plotSamples(self):
        self.graph1.clear()
        # sampling the signal with a sampling rate of 80 Hz
        # in this case, we are using the Nyquist rate.
        f = 40;  # Hz
        tmin = -1
        tmax = 1
        T = 1 / self.horizontalSlider.value()
        nmin = ceil(tmin / T)
        nmax = floor(tmax / T)
        n = arange(nmin, nmax)
        x1 = cos(2 * pi * n * T) + cos(2 * pi * f * n * T)
        self.graph1.plot(n * T, x1, symbol='o', pen='b')

    def plotSeparateSamples(self):
        self.graph2.clear()
        f = 40;  # Hz
        tmin = -1;
        tmax = 1;
        T = 1 / self.horizontalSlider.value();
        nmin = ceil(tmin / T);
        nmax = floor(tmax / T);
        n = arange(nmin, nmax);
        x1 = cos(2 * pi * n * T) + cos(2 * pi * f * n * T);
        self.graph2.plot(n * T, x1, pen='b')
    def clear(self):
        self.splitter.setGeometry(QtCore.QRect(60, 10, 610, 1300))
        self.splitter.setOrientation(QtCore.Qt.Vertical)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()