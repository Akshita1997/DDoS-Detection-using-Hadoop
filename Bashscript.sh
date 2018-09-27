#!/bin/bash  
sudo tshark -a duration:10 | hadoop fs -put - /tshark38
sudo /usr/local/hadoop-2.8.1/bin/hadoop jar /home/arushi/hadoop-streaming-2.8.1.jar -mapper /home/arushi/Desktop/files/python-nltk/DDoS/mapper.py -reducer /home/arushi/Desktop/files/python-nltk/DDoS/reducer.py -input /tsharkf -output /user/outputf
for i in {1..9}
	do
		sudo tshark -a duration:10 | hadoop fs -put -f - /tshark1
		sudo /usr/local/hadoop-2.8.1/bin/hadoop fs -cat /tshark1 | hadoop fs -appendToFile - /tsharkf

		sudo /usr/local/hadoop-2.8.1/bin/hadoop jar /home/arushi/hadoop-streaming-2.8.1.jar -mapper /home/arushi/Desktop/files/python-nltk/DDoS/mapper.py -reducer /home/arushi/Desktop/files/python-nltk/DDoS/reducer.py -input /tshark1 -output /user/output1
		sudo /usr/local/hadoop-2.8.1/bin/hadoop fs -cat /user/output1/part-00000 | hadoop fs -appendToFile - /user/outputf/part-00000
		sudo /usr/local/hadoop-2.8.1/bin/hadoop fs -rmr /user/output1
	done
