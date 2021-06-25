### Repository information
In this repository we find the delivery of the Lab 3 of the Audio and Video Encoding Systems subject (video part).

We have 5 .py files and in each of them we find a detailed explanation on how to use them:

## **ex1.py**
In this script we enter the name of the video "Big Buck Bunny", trim the first minute and generate the following files:
- An mp3 file with the audio in mono format.
- An mp3 file with the audio with a bit rate of 24kb.
- An mp4 file with the 1 minute video and the subtitles.

Once we have generated all these files, we create a container where we combine all of them.
Below we see the resulting content:

<img src="https://drive.google.com/uc?export=view&id=1zFBKjD37DKAEZkDnguHInbi9Qq6zKxLn" width="500">


## **ex2.py**
Using this script, we can generate a custom container automatically. When we run it, we enter the number of files that we will insert in the container and for each of them we insert the name and the number of channels it has.

When we finish inserting the information we generate the container.

In the following image we see the result of generating a container with the two audio files from the previous section:

<img src="https://drive.google.com/uc?export=view&id=1-_GNXOlCRv5MD8Fj4tL7b_Na4bK87LqD" width="500">


## **ex3.py**
In this script we enter the name of a container and get which of the broadcast formats would be supported to send it (DVB, ISDB, ATSC, DTMB) or an error message in case there is none.

The result we get for the container in the first section is as follows:

<img src="https://drive.google.com/uc?export=view&id=1UUExRy7kMKfZESqQuFIhQl0_Ktak8sGm" width="500">


## **ex4.py**
In this script we simply call script 2 and consicutively script 3, so we generate a custom container and look at what broadcast formats it is compatible with.


## **ex5.py**
Finally we have a script that contains a class through which we can access functions that allow us to run the previous scripts.  


<img src="https://drive.google.com/uc?export=view&id=15NLUzS6RGqkMxtHm0hzqKLw6MS3uotnQ" width="500">
