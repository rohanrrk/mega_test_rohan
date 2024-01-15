Test 1: AWS S3

Programming Language Used: Python(For measuring the upload perf and generating the perf report), JS for uploading the file to S3 bucket and for web app

# Steps to run:

1. Once the code is cloned you need to run ``` pip install -r requirements.txt```
2. To verify the upload speed you need to first specify your access key and secret access key along with bucket name in the javascript file (location /mega_test1_s3_bucket/static.app.js. More info can be found on how to add the keys, bucket name, region in js file). Make sure you create a folder  inside s3 bucket named as Document where the web app will upload the txt file.
3. To start the webapp run ```flask --app app.py run```
4. After the upload, Python function startspeedtest() in app.py  will be responsible for monitoring the upload performance and writing the speed in csv file which will be present in results directory
5. Once upload is completed goto results directory and run ```python3 plot.py test.csv```. This will generate a performance jpg file for s3 file upload operation

Video POC: https://vimeo.com/902893167?ts=0&share=copy (Video Password: Qawzsx!123)

