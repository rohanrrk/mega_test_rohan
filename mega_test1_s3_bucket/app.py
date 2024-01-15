from flask import Flask, render_template
import speedtest
import datetime
import csv,time
from multiprocessing import Process

app = Flask(__name__, static_url_path='/static') 
global_process_obj = None

@app.route('/')
def home():
        return render_template('index1.html')

def startspeedtest():
	s = speedtest.Speedtest(secure=True)
	with open('result/test.csv', mode='w', newline='') as speedcsv:
    		csv_writer = csv.DictWriter(speedcsv,fieldnames=['time',  'upspeed'])
    		csv_writer.writeheader()
    		while True:
        		time = datetime.datetime.now().strftime("%H:%M:%S")
        		upspeed = round((round(s.upload()) / 1048576), 2)
        		csv_writer.writerow({
            			'time': time,
            			"upspeed": upspeed})
        		speedcsv.flush()

@app.route("/start", methods=['POST'])
def starttestbutton():
	global global_process_obj
	global_process_obj = Process(target = startspeedtest)
	global_process_obj.start()
	return render_template('index.html')

@app.route("/stop",methods=['GET'])
def killspeedtestprocess():
	time.sleep(10)
	global_process_obj.terminate()
	return "Process Terminated! Run the plot.py on the result csv file to generate the report"

if __name__ == '__main__':
	app.run()
