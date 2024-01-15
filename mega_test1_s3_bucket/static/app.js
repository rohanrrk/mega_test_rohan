 var bucket = new AWS.S3({
   accessKeyId: "AKIA4MTWNRJPDGG4NPHK", //enter your access key id for s3 bucket access
   secretAccessKey: "OkfbtCkmHG8AMoJ2elW0bxvL5Y1bfv8FhDqPKHpL",  //enter your access key secret for s3 bucket access
   //sessionToken: "SESSION_TOKEN", // optional you can remove if you don't want pass
   region: 'us-east-1' //enter your s3 bucket region
 });

 uploadfile = function(fileName, file, folderName) {
   const params = {
     Bucket: "mega-assignment-s3-bucket",  //enter your bucket name
     Key: folderName + fileName,
     Body: file,
     ContentType: file.type
   };
   return bucket.upload(params, function(err, data) {

     if (err) {
       console.log('There was an error uploading your file: ', err);
       return false;
     }
     console.log('Successfully uploaded file.', data);
     return true;
   });
 }

 uploadSampleFile = function() {
   var progressDiv = document.getElementById("myProgress");
   progressDiv.style.display="block";
   var progressBar = document.getElementById("myBar");
   file = document.getElementById("myFile").files[0];
   folderName = "Document/";  //create a folder inside your bucket with name document
   uniqueFileName = 'SampleFile';  //this is the name of the file that will given when data is uploaded in s3
   let fileUpload = {
     id: "",
     name: file.name,
     nameUpload: uniqueFileName,
     size: file.size,
     type: "",
     timeReference: 'Unknown',
     progressStatus: 0,
     displayName: file.name,
     status: 'Uploading..',
   }
   uploadfile(uniqueFileName, file, folderName)
     .on('httpUploadProgress', function(progress) {
       let progressPercentage = Math.round(progress.loaded / progress.total * 100);
       console.log(progressPercentage);
       progressBar.style.width = progressPercentage + "%";
       if (progressPercentage < 100) {
         fileUpload.progressStatus = progressPercentage;

       } else if (progressPercentage == 100) {
         fileUpload.progressStatus = progressPercentage;
         fileUpload.status = "Uploaded";
       }
     })
 }

