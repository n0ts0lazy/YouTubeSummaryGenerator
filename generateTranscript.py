from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def generateTranscript(vidID):
    print('Getting original transcript from www.youtube.com')
    global clipBoard1
    global clipBoard2
    #calling the API to request for transcript
    sourceExtraction= YouTubeTranscriptApi.get_transcript(vidID)
    #using built in formatter tool that can be used to get the return type as a string
    sourceText= TextFormatter()
    #using preformatting tool
    sourceTextExtract= sourceText.format_transcript(sourceExtraction)
    sourceToRead= ""
    sourceTextFilter=[]
    #cleaning the source to create a single string without any line break so that it can be used in summarization tool since it has no purpose in it
    for lead in sourceTextExtract:
        sourceTextFilter.append(lead.replace('\n',' '))    
    for lead in sourceTextFilter:
        sourceToRead += lead
    clipBoard1=sourceTextExtract
    clipBoard2=sourceToRead    

clipBoard1=""
clipBoard2=""