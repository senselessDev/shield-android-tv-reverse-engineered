import numpy
import matplotlib.pyplot

data = numpy.load('boot.npy')

matplotlib.pyplot.plot(data)
matplotlib.pyplot.show()

threshold = 100
th_applied = numpy.array(data > threshold, dtype=numpy.uint8)

numpy.savetxt('threshold_applied.csv', th_applied, delimiter = ';', fmt='%i')
