Author: Yash Hemant Jain
Net Id: yxj180004
CS 6322.001 Information Retrieval
Homework-3

Resources Used: Wordnet Lemmatizer, Stopwords, Averaged_perceptron_tagger from nltk library.


Files: Ranking.py, Cranfield directory and hw3.queries
Python version used: 2.7.5(UTD Server), 3.6 (personal machine)

STEPS for Execution:

1. Open the terminal (e.g. putty)
2. Login to the hostname csgrads1.utdallas.edu with the UTD Netid Credentials.
3. Copy the file ranking.py onto the server using ftp (e.g. using ftp applications like FileZilla)
4. Change the file permissions by using 'chmod' command like
	{csgrads1:~} chmod 777 ranking.py

5. Install nltk, command:{csgrads1:~} pip install nltk --user
6. Import Wordnet Lemmatizer, Stopwords libraries by running the following command:
	{csgrads1:~} python
	>>> import nltk
   	>>> nltk.download('punkt')
	>>> nltk.download('stopwords')
	>>> nltk.download('wordnet')
	>>> nltk.download('averaged_perceptron_tagger')
	
5. Run the ranking.py file passing Cranfield directory path and query file path under single quotes as a command line argument like
	{csgrads1:~} python ranking.py '/people/cs/s/sanda/cs6322/Cranfield' '/people/cs/s/sanda/cs6322/hw3.queries'
6. The output will get printed on the terminal console.