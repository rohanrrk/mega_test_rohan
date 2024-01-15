import matplotlib.pyplot as plt
import csv,os
from datetime import datetime,date
import matplotlib.ticker as ticker
times = []
upload = []

current_time = datetime.now()
current_time = current_time.strftime("%H:%M:%S")
today = date.today()
date_time = "S3 upload performance report - "+str(today)+"_"+str(current_time)
rename_command = "mv test_graph.jpg "+str(today)+"_"+str(current_time)+".jpg"
with open('test.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        times.append(str(row[0]))
        upload.append(float(row[1]))

report = "S3 upload speed test report"
plt.figure('S3 upload speed test report', [30, 30])
plt.plot(times, upload, label='upload', color='g')
plt.xlabel('time')
plt.ylabel('speed in Mb/s')
plt.title(date_time)
plt.legend()
plt.savefig('test_graph.jpg', bbox_inches='tight')
os.system(rename_command)
os.system("rm test.csv")

