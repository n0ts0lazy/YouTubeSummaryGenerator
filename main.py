#All used libraries along with dependency and linking
import os
import warnings
import time

from datetime import datetime

import generateSummary
import generateTranscript
import similarityCheck

def linkType(vidurl):
    '''
    Here we are determining the type of link by checking specific position in the link which
    can be used to determine the type of link and if not valid will exit the program else will return the
    video id to the main program
    '''	
    global vidKey
    #start at 22
    if vidurl[8]== 'w':
        vidKey= vidurl[32:]
        print("Provided link:", vidurl,"\nVideo ID obtained:",vidKey,"\nLink Type: Normal Web Address\n")
        return vidKey
    elif vidurl[8]== 'y' or vidurl[0]== 'y':
        if vidurl[0]== 'y':
            vidKey=vidurl[9:]
        elif vidurl[8]== 'y':
            vidKey= vidurl[17:]
        print("Provided link:", vidurl,"\nVideo ID obtained:",vidKey,"\nLink Type: Short Youtube Address\n")
        return vidKey
    else:
        print("Sorry Link Not Available, Enter Link Only In Format:\nhttps://youtube.com/watch?v=<video link> (or) youtu.be/<video link> (or) https://youtu.be/<video link>\nYouTube Shorts are not supported by this program")
        exit()

def ignoreWarnings():
    warnings.filterwarnings("ignore")

def preRunCheck():
    '''
    Here we create the necessary folders for the execution since if executing for first time we get error if no folders exist
    and we also create the file where we must provide the input that will be used to get the video id
    '''
    print('Checking prerequisites\n')
    if os.path.isdir('export/text')==False:
        os.makedirs('export/text')
    if os.path.isdir('export/result')==False:
        os.makedirs('export/result')
    if os.path.isfile("paste link here.txt")== True:
        print("Reading from \"paste link here.txt\" please wait...\n")
        return
    with open ("paste link here.txt",'w',encoding='utf-8') as textFile:
        textFile.write("Enter your video URL: ")
    print("Write the link of video in \"paste link here.txt\" and run the program again")  
    exit()

def performCleanup():
    #Cleans up the temporary files created during execution freeing up space
    print("All operations completed successfully.\nCheck \\export\\text for Text version of export\n")
    time.sleep(3)
    print("Performing Cleanup, please wait.")
    os.remove("paste link here.txt")
    os.remove('buffer.txt')
    time.sleep(3)

def exportText(clipBoard, fileType):
    #Export any of the generated string into a text file
    global fileNameTemplate
    with open ('./export/text/'+fileType+' '+fileNameTemplate+'.txt','w',encoding='utf-8') as textFile:
        textFile.write(clipBoard)

def generateReport():
    #This is only to generate output for the similarityCheck script since this has to access a temporary file for the files to be written
    with open('buffer.txt','r',encoding='utf-8') as textFile:
        clipBoard=textFile.read()
    with open('./export/result/Report '+fileNameTemplate+'.txt','w',encoding='utf-8') as textFile:
        textFile.write(clipBoard)
    
startTime= time.time()

preRunCheck()
ignoreWarnings()

fileNameTemplate = datetime.now().strftime("%d,%h,%y-%H.%M.%S")

with open ("paste link here.txt",'r',encoding='utf-8') as textFile:
    linkLookup=textFile.read()

clipBoard= ""
vidKey= ""
linkLookup=linkLookup[22:]

linkType(linkLookup)
generateTranscript.generateTranscript(vidKey)
clipBoard= generateTranscript.clipBoard1
exportText(clipBoard,"Original Transcript "+vidKey+' ')

clipBoard=generateTranscript.clipBoard2
generateSummary.generateSummary(clipBoard)
generateSummary.prepareForExport(generateSummary.clipBoard1)

clipBoard= generateSummary.longstr
exportText(clipBoard,"Summary "+vidKey+' ')

similarityCheck.performSimilarityCheck(generateTranscript.clipBoard1, generateSummary.longstr)
generateReport()

performCleanup()

runTime= time.time()
runTime= str(runTime-startTime)
print('Total execution time: '+runTime[:5]+' seconds')
time.sleep(5)