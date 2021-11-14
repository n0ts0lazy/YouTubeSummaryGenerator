from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def generateTranscript(vidID):
    print('Getting original transcript from www.youtube.com')
    global clipBoard1
    global clipBoard2
    sourceExtraction= YouTubeTranscriptApi.get_transcript(vidID)
    sourceText= TextFormatter()
    sourceTextExtract= sourceText.format_transcript(sourceExtraction)
    sourceToRead= ""
    sourceTextFilter=[]
    for lead in sourceTextExtract:
        sourceTextFilter.append(lead.replace('\n',' '))    
    for lead in sourceTextFilter:
        sourceToRead += lead
    clipBoard1=sourceTextExtract
    clipBoard2=sourceToRead    

clipBoard1=""
clipBoard2=""

