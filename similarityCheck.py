import pandas
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from gensim.matutils import cossim
from gensim import corpora
from gensim.utils import simple_preprocess


def performSimilarityCheck(sourceText, summaryText):
    print('Comparing original transcript to summary for similarity using cosine similarity')
    sources=[sourceText,summaryText]
    countVectorizer= CountVectorizer(stop_words='english')
    countVectorizer= CountVectorizer()
    sparseMatrix= countVectorizer.fit_transform(sources)
    print(str(sparseMatrix))

    termsMatrix= sparseMatrix.todense()
    print(str(termsMatrix))
    frame= pandas.DataFrame(termsMatrix,columns=countVectorizer.get_feature_names_out(),index=['source','generated'])
    print(str(frame))
    textFile= open('buffer.txt','a',encoding='utf-8')
    textFile.write('Confusion Matrix: \n')
    textFile.close()
    with open ('buffer.txt','a',encoding='utf-8') as textFile:
        textFile.write(str(cosine_similarity(frame,frame)))
    textFile= open('buffer.txt','a',encoding='utf-8')
    textFile.write('\n\nCosine Similarity: ')
    textFile.close()
    dictionary= corpora.Dictionary([simple_preprocess(reader) for reader in sources])
    print(str(dictionary))
    sentenceBagSource= dictionary.doc2bow(simple_preprocess(sourceText))
    print(str(sentenceBagSource))
    sentenceBagSummary= dictionary.doc2bow(simple_preprocess(summaryText))
    print(str(sentenceBagSummary))
    textFile= open('buffer.txt','a',encoding='utf-8')
    textFile.write(str(cossim(sentenceBagSource,sentenceBagSummary))+'\n')
    if cossim(sentenceBagSource,sentenceBagSummary) >= 0.75:
        textFile.write("\nThe generated summary is mostly similar to the original content")
    elif cossim(sentenceBagSource,sentenceBagSummary)== 0:
        textFile.write("\nThe generated summary is not similar at all")
    else:
        textFile.write("\nThe generated summary is partially similar to the original content")
    textFile.close()
    print('Report generated at \\export\\result\n')
    

