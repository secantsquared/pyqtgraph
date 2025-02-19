# -*- coding: utf-8 -*-
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from time import perf_counter

app = pg.mkQApp()
plt = pg.PlotWidget()

app.processEvents()

## Putting this at the beginning or end does not have much effect
plt.show()   

## The auto-range is recomputed after each item is added,
## so disabling it before plotting helps
plt.enableAutoRange(False, False)

def plot():
    start = perf_counter()
    n = 15
    pts = 100
    x = np.linspace(0, 0.8, pts)
    y = np.random.random(size=pts)*0.8
    for i in range(n):
        for j in range(n):
            ## calling PlotWidget.plot() generates a PlotDataItem, which 
            ## has a bit more overhead than PlotCurveItem, which is all 
            ## we need here. This overhead adds up quickly and makes a big
            ## difference in speed.
            
            #plt.plot(x=x+i, y=y+j)
            plt.addItem(pg.PlotCurveItem(x=x+i, y=y+j))
            
            #path = pg.arrayToQPath(x+i, y+j)
            #item = QtGui.QGraphicsPathItem(path)
            #item.setPen(pg.mkPen('w'))
            #plt.addItem(item)
            
    dt = perf_counter() - start
    print(f"Create plots tooks {dt * 1000:.3f} ms")

## Plot and clear 5 times, printing the time it took
for i in range(5):
    plt.clear()
    plot()
    app.processEvents()
    plt.autoRange()





def fastPlot():
    ## Different approach:  generate a single item with all data points.
    ## This runs about 20x faster.
    start = perf_counter()
    n = 15
    pts = 100
    x = np.linspace(0, 0.8, pts)
    y = np.random.random(size=pts)*0.8
    xdata = np.empty((n, n, pts))
    xdata[:] = x.reshape(1,1,pts) + np.arange(n).reshape(n,1,1)
    ydata = np.empty((n, n, pts))
    ydata[:] = y.reshape(1,1,pts) + np.arange(n).reshape(1,n,1)
    conn = np.ones((n*n,pts))
    conn[:,-1] = False # make sure plots are disconnected
    path = pg.arrayToQPath(xdata.flatten(), ydata.flatten(), conn.flatten())
    item = QtGui.QGraphicsPathItem(path)
    item.setPen(pg.mkPen('w'))
    plt.addItem(item)
    
    dt = perf_counter() - start
    print("Create plots took: %0.3fms" % (dt*1000))


## Plot and clear 5 times, printing the time it took
if hasattr(pg, 'arrayToQPath'):
    for i in range(5):
        plt.clear()
        fastPlot()
        app.processEvents()
else:
    print("Skipping fast tests--arrayToQPath function is missing.")

plt.autoRange()

if __name__ == '__main__':
    pg.exec()
