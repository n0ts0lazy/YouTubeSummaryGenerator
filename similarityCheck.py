import pandas
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from gensim.matutils import cossim
from gensim import corpora
from gensim.utils import simple_preprocess


def performSimilarityCheck(sourceText, summaryText):
    print('Comparing original transcript to summary for similarity using cosine similarity')
    #Creating a sentence pool
    sources=[sourceText,summaryText]
    #seperating words based on its count from each sentence pool
    countVectorizer= CountVectorizer(stop_words='english')
    countVectorizer= CountVectorizer()
    #Creating Sparse Matrix
    sparseMatrix= countVectorizer.fit_transform(sources)

    termsMatrix= sparseMatrix.todense()
    #Converting to dataframe
    frame= pandas.DataFrame(termsMatrix,columns=countVectorizer.get_feature_names_out(),index=['source','generated'])
    textFile= open('buffer.txt','a',encoding='utf-8')
    textFile.write('Similarity Matrix: \n')
    textFile.close()
    #Creating similarity matrix from the dataframe created
    with open ('buffer.txt','a',encoding='utf-8') as textFile:
        textFile.write(str(cosine_similarity(frame,frame)))
    textFile= open('buffer.txt','a',encoding='utf-8')
    textFile.write('\n\nCosine Similarity: ')
    textFile.close()
    #Preprocessing words into a dictionary and converting all the sentences into a bag to be processed easily based on frequency of it being used
    dictionary= corpora.Dictionary([simple_preprocess(reader) for reader in sources])
    sentenceBagSource= dictionary.doc2bow(simple_preprocess(sourceText))
    sentenceBagSummary= dictionary.doc2bow(simple_preprocess(summaryText))
    textFile= open('buffer.txt','a',encoding='utf-8')
    textFile.write(str(cossim(sentenceBagSource,sentenceBagSummary))+'\n')
    #Determining the similarity of the original content from the created summary
    if cossim(sentenceBagSource,sentenceBagSummary) >= 0.75:
        textFile.write("\nThe generated summary is mostly similar to the original content")
    elif cossim(sentenceBagSource,sentenceBagSummary)== 0:
        textFile.write("\nThe generated summary is not similar at all")
    else:
        textFile.write("\nThe generated summary is partially similar to the original content")
    textFile.close()
    print('Report generated at \\export\\result\n')
    