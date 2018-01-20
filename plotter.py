import numpy, matplotlib, datetime, matplotlib.pyplot as plt
from dateutil import tz
import matplotlib.dates as mdates

data = numpy.loadtxt("outfile.txt", usecols=(2, 5, 8, 11, 14, 17))
dates = numpy.loadtxt("outfile.txt", usecols=[0,], dtype="S")
times = numpy.loadtxt("outfile.txt", usecols=[1,], dtype="S")
datetimes = [datetime.datetime.strptime(d+t, "%Y-%m-%d%H:%M:%S.%f") for d,t in zip(dates,times)]
# datetimes = [dt.replace(tzinfo=tz.tzutc()) for dt in datetimes]
# datetimes = [dt.astimezone(tz.tzlocal()) for dt in datetimes]
datetimes = matplotlib.dates.date2num(datetimes)
plt.plot_date(datetimes, data, ".", tz='US/Pacific')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
plt.gcf().autofmt_xdate()
plt.show()
