# SGX-API-first-app
This is a simple app to illustrate API calls inside an SGX application.  
  
The goal is to be able to use data from an API inside some calculations inside an SGX enclave. In this app, we call an API from https://aqicn.org/api/ to get some information about the air quality.

To run this application using the iExec platform, you can follow the tutorials from https://docs.iex.ec/for-developers/confidential-computing/create-your-first-sgx-app using the code from this repository instead of the scone-hello-world one (https://github.com/iExecBlockchainComputing/scone-hello-world-app).  
  
Don't forget to ask for your own API key and add it to the API call (/src/app.py l.23).
