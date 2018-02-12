import gensim
from nltk.tokenize import word_tokenize


# Has all the training corpus
descriptions = [
                "When a pilot crashes and tells of conflict in the outside world, Diana, an Amazonian warrior in training, leaves home to fight a war, discovering her full powers and true destiny.",
                "Fearing that the actions of Superman are left unchecked, Batman takes on the Man of Steel, while the world wrestles with what kind of a hero it really needs.",
                "A thief, who steals corporate secrets through the use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO."
                "The absurd antics of an Indiana town's public officials as they pursue sundry projects to make their city a better place.",
                "Almost two years after a virus wiped out most of the human race, Phil Miller only wishes for some company, but soon gets more than he bargained for when that company shows up in the form of other survivors.",
                "In a world where mutated humans are treated with distrust and fear, an institute for mutants battles to achieve peaceful co-existence with humanity.",
                "The boundaries between military discipline and human desire are tested on a U.S. Army base that houses an elite unit of helicopter pilots trained to perform clandestine international and domestic missions.",
                "Jane Doe is found in Times Square with no memory and mysterious tattoos on her body.",
                "A remote Alaskan town that has been overrun by paranormal forces and local outcast Roman Mercer (Jogia) must overcome the town's prejudices and his own personal demons if he's to harness his repressed psychic powers and save everyone from the mass haunting that's threatening to destroy them all.",
                "Follows a locally born and bred S.W.A.T. lieutenant who is torn between loyalty to the streets and duty to his fellow officers when he's tasked to run a highly-trained unit that's the last stop for solving crimes in Los Angeles.",
                "Anthology television series based on Steven Soderbergh's 'The Girlfriend Experience.'",
                "An anthology series exploring a twisted, high-tech world where humanity's greatest innovations and darkest instincts collide.",
                "A notorious gang in 1919 Birmingham, England, is led by the fierce Tommy Shelby, a crime boss set on moving up in the world no matter the cost."
               ]

#
# function that takes in all the descriptions from various
#
def getModel():

    # conveniently splits the text into whatever that is required
    splitDescriptions = [[w.lower() for w in text.replace("(", " ").replace(")", " ").replace(",", " ").replace(".", " ").split()] for text in descriptions]

    dictionary = gensim.corpora.Dictionary(splitDescriptions) # create the dictionary
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in splitDescriptions] # use the corpus
    tf_idf = gensim.models.TfidfModel(corpus) # the model is intialized
    sims = gensim.similarities.Similarity('~/Documents/NLP', tf_idf[corpus], num_features=len(dictionary)) # creates the similarity file
    # returns all the required variables
    return tf_idf, dictionary, sims