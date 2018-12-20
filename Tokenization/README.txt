Author: Yash Hemant Jain
Net Id: yxj180004
CS 6322.001 Information Retrieval

Resources Used: (Stemming.py) PorterStemmer immplementation by Vivake Gupta, url: https://tartarus.org/martin/PorterStemmer/python.txt
Files: Tokenize.py, Stemming.py, Cranfield directory
Python version used: 2.7.5(UTD Server), 3.6 (personal machine)

STEPS for Execution:

1. Open the terminal (e.g. putty)
2. Login to the hostname csgrads1.utdallas.edu with the UTD Netid Credentials.
3. Copy the files Tokenize.py and Stemming.py onto the server using ftp (e.g. using ftp applications like FileZilla)
4. Change the file permissions by using 'chmod' command like
	{csgrads1:~} chmod 777 Tokenize.py
	{csgrads1:~} chmod 777 Stemming.py
5. Run the Tokenize.py file passing Cranfield directory path under single quotes as a command line argument like
	{csgrads1:~} python Tokenize.py '/people/cs/s/sanda/cs6322/Cranfield'
6. The output will get printed on the terminal console.