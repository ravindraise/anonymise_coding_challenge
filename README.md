This code will take generate the csv data required for anonymize the PII data like first name, last name and address
1) Input for the python code is no of rows csv data to be generated . ex: 500,1000 etc
2) Python code will output the following
    a) Save the generated input csv data in current working dir
    b) Save the anonymized csv file in the current working dir
3) Python code will  anonymize the input data for the columns 'first_name', 'last_name', 'address' using
    a) Sha256 algorithm 
    b) Using random values for ascii and degits

4) I have created a docker image to run

5) Also the folder contains the sample input and output files created from sample run.
