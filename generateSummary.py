import math
import warnings

from transformers import pipeline

def generateSummary(clipBoard):
    print('Preparing the transcript for summary generation')
    warnings.filterwarnings('ignore')
    global longstr
    longstr=clipBoard
    textProcessLimit=1000
    textBatchDivision=len(longstr)/1000
    if textBatchDivision > math.floor(textBatchDivision):
        textBatchDivision=math.floor(textBatchDivision)+1
    summarize=pipeline("summarization")
    print('Generating Summary\n')

    for index in range(1,textBatchDivision):
        summaryGenerated=summarize(longstr[:index*textProcessLimit])[0]['summary_text']
        clipBoard1.append(summaryGenerated)

def prepareForExport(clipBoard):
    global longstr
    longstr= ""
    for summaryPart in clipBoard:
        longstr+=summaryPart


longstr=""
clipBoard1=[]
