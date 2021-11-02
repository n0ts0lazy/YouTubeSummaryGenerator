import math
import warnings

from transformers import pipeline

def generateSummary(clipBoard):
    print('Preparing the transcript for summary generation')
    warnings.filterwarnings('ignore')
    global longstr
    longstr=clipBoard
    #limiting the word process limit to 1000 because pipeline has a character limit to be processed at 1024 words
    textProcessLimit=1000
    textBatchDivision=len(longstr)/1000
    #to handle edge cases where if a value is >x.5 the floor will be x instead of x+1
    if textBatchDivision > math.floor(textBatchDivision):
        textBatchDivision=math.floor(textBatchDivision)+1
    #tokenizing the information into token
    summarize=pipeline("summarization")
    print('Generating Summary\n')

    for index in range(1,textBatchDivision):
        #summarizing text per batch
        summaryGenerated=summarize(longstr[:index*textProcessLimit])[0]['summary_text']
        clipBoard1.append(summaryGenerated)

def prepareForExport(clipBoard):
    #since the text was summarized in batch now it is stored in form of list so converting it back to a single string for easier usage in future reference
    global longstr
    longstr= ""
    for summaryPart in clipBoard:
        longstr+=summaryPart


longstr=""
clipBoard1=[]
