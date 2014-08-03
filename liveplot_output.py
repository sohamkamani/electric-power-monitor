import serial
import sys, serial
import numpy as np
from time import sleep
from collections import deque
from matplotlib import pyplot as plt



class AnalogData:
  # constr
  def __init__(self, maxLen):
    self.ax = deque([0.0]*maxLen)
    self.maxLen = maxLen
 
  # ring buffer
  def addToBuf(self, buf, val):
    if len(buf) < self.maxLen:
      buf.append(val)
    else:
      buf.pop()
      buf.appendleft(val)
 
  # add data
  def add(self, data):
    self.addToBuf(self.ax, data)
    
# plot class
class AnalogPlot:
  # constr
  def __init__(self, analogData):
    # set plot to animated
    plt.ion() 
    self.axline, = plt.plot(analogData.ax)
    plt.ylim([0, 100])
 
  # update plot
  def update(self, analogData):
    self.axline.set_ydata(analogData.ax)
    plt.pause(.001)
    plt.draw()



def main():
 
  # plot parameters
  analogData = AnalogData(100)
  analogPlot = AnalogPlot(analogData)
  
 
  print 'plotting data...'
 
  # open serial port
  ser = serial.Serial("COM5", 9600)
  data=0;
  ylimit=0;
  while True:
    try:
        line = ser.readline()
        print line
        try:
          data= int(line);
          if(data>ylimit):
            plt.ylim([0,(data+10)]);
            ylimit=data+10;
        except:
          data=data
        analogData.add(data)
        analogPlot.update(analogData)
    except KeyboardInterrupt:
      print 'exiting'
      break
  # close serial
  ser.flush()
  ser.close()
 
# call main
if __name__ == '__main__':
  main()
