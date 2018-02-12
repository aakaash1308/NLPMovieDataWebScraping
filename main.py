import gensim
import getWebData
import trainModel

# Load Google's pre-trained Word2Vec model.
#model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

#print(getWebData.getData())


#
# function that takes in the url data and predicts the most probable description
#
def printProbableDescription(text, real):
    max = -1 # going to store the max of all the sentences
    index = 0 # going to store the index of the max index

    # get the training model
    tf_idf, dictionary, sims = trainModel.getModel()

    # going through each sentence
    for i in range(0, len(text)):
        query_doc_bow = dictionary.doc2bow(text[i]) # convert to a dictionary
        query_doc_tf_idf = tf_idf[query_doc_bow] # getting all the counts and the similarities
        sum = 0
        for j in sims[query_doc_tf_idf]: # going and adding each file's probability for the sentence
            sum += j
         # averaging each sentence's score
        sum = sum/len(text)
        if (sum > max): # getting the max
            max = sum
            index = i

    print(" ".join(real[index].split())) # returns the real sentence or hopefully description



# get the url data in list of lists
text, real = getWebData.getData()

# going through each url and tries to predict the best one
for i in range(0, len(text)):
    printProbableDescription(text[i], real[i])





