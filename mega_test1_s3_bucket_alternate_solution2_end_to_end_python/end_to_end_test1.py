import boto3
import imp,os,time,csv
from datetime import datetime,date
from multiprocessing import Process
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import speedtest

class s3testmega:

	def __init__(self,prop_file):
		self.filename = prop_file
		self.props = ''
		self.s3_client_obj = ''
		self.process_obj = ''

	def initialize_prop_file(self):
		''' Initialize props like aws s3 key and secret '''

		fileobj = open(self.filename)
		self.props = imp.load_source('data', self.filename ,fileobj )
		fileobj.close()

	def create_bucket(self):
		''' Create S3 Bucket '''

		print("Step1. Creating the bucket")
		self.s3_client_obj =  boto3.client('s3',aws_access_key_id=self.props.aws_access_key_id_value,aws_secret_access_key=self.props.aws_secret_access_key_value)
		response = self.s3_client_obj.create_bucket(Bucket=self.props.bucket_value)

	def start_perf_monitoring(self):
		''' Start perf monitoring '''

		s = speedtest.Speedtest(secure=True)
		with open('result/test.csv', mode='w', newline='') as speedcsv:
			csv_writer = csv.DictWriter(speedcsv,fieldnames=['time',  'upspeed'])
			csv_writer.writeheader()
			while True:
				time = datetime.now().strftime("%H:%M:%S")
				upspeed = round((round(s.upload()) / 1048576), 2)
				csv_writer.writerow({
                                	'time': time,
                                	"upspeed": upspeed})
				speedcsv.flush()

	def upload_file(self,file_path, file_name):
		''' upload the test file '''

		print("Step2. Uploading the file to s3 bucket")
		full_path = os.path.join(file_path,file_name) 
		self.s3_client_obj.upload_file(full_path,self.props.bucket_value, file_name)

	def download_file_s3(self, s3_file_name, download_path):
		''' Download the file from s3 bucket '''

		print("Step3. Downloading the file from s3 bucket") 
		full_path = os.path.join(download_path,s3_file_name)
		self.s3_client_obj.download_file(self.props.bucket_value,s3_file_name, full_path)

	def delete_file_s3(self,s3_file_name):
		''' Delete file from s3 bucket  '''

		print("Step4. Deleting the s3 file")
		self.s3_client_obj.delete_object(Bucket=self.props.bucket_value, Key=s3_file_name)

	def start_perf_process(self):
		''' start perf monitoring '''

		print("Starting upload monitoring process")
		self.process_obj = Process(target = self.start_perf_monitoring)
		self.process_obj.start()

	def stop_perf_process(self):
		''' stop perf monitoring '''

		print("Stopping upload monitoring process")
		time.sleep(10)
		self.process_obj.terminate()


	def create_file_upload_report(self):
		''' Create file upload perf report '''
		times = []
		upload = [] 
		print("Step5. Generating perf upload report for s3")
		current_time = datetime.now()
		current_time = current_time.strftime("%H:%M:%S")
		today = date.today()
		date_time = "S3 upload performance report - "+str(today)+"_"+str(current_time)
		rename_command = "mv result/test_graph.jpg result/perf_"+str(today)+"_"+str(current_time)+".jpg"
		with open('result/test.csv', 'r') as csvfile:
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
		plt.savefig('result/test_graph.jpg', bbox_inches='tight')
		os.system(rename_command)
		os.system("rm result/test.csv")

if __name__ == "__main__":

	''' Test case steps '''

	s3testmegaobj = s3testmega('./prop.env')
	s3testmegaobj.initialize_prop_file()
	s3testmegaobj.create_bucket()
	s3testmegaobj.start_perf_process()
	s3testmegaobj.upload_file('file_to_upload', 'test_file.txt')
	s3testmegaobj.stop_perf_process()
	s3testmegaobj.download_file_s3('test_file.txt','downloads')
	s3testmegaobj.delete_file_s3('test_file.txt')
	s3testmegaobj.create_file_upload_report()
