import matplotlib
matplotlib.use('agg')
import numpy, datetime, matplotlib.pyplot as plt
from dateutil import tz
import matplotlib.dates as mdates


data = numpy.genfromtxt("outfile.txt", usecols=(2, 3, 4, 5, 6, 7), delimiter=" ",
                        missing_values = "FULL", filling_values = 0,
                        autostrip = True)
dates = numpy.loadtxt("outfile.txt", usecols=[0,], dtype="S")
times = numpy.loadtxt("outfile.txt", usecols=[1,], dtype="S")
datetimes = [datetime.datetime.strptime(d+t, "%Y-%m-%d%H:%M:%S.%f") for d,t in zip(dates,times)]
datetimes = matplotlib.dates.date2num(datetimes)
plt.plot_date(datetimes, data, "-")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
plt.gcf().autofmt_xdate()
plt.savefig("out.png")
