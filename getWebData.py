import urllib3
from bs4 import BeautifulSoup
import re

# required to get the link for the data
urls = ["http://www.imdb.com/title/tt3107288/?ref_=nv_sr_1", "http://www.imdb.com/title/tt2193021/?ref_=nv_sr_1"] # the links for the websites

#
# takes in an html string and cleans it to be able to make it usable
#
def makeClean(html):
    # cleaning all the non required characters
    temp = html.replace("<", ":").replace(">", ":").replace("\n", ":").replace("=", ":").replace("\"",":").replace("\\", ":").replace(";", ":").replace("-", ":").split(":")
    out = []
    realSentence = []
    for i in range(0, len(temp)):
        if (len(temp[i].split()) > 10): # assuming description will have at least 10 words
            realSentence += [temp[i]]
            out += [" ".join(temp[i].split()).replace("(", " ").replace(")", " ").replace(",", " ").replace(".", " ").split()] # converts many spaces to one space
    return out, realSentence

#
# returns the data from each of the urls in a list of lists
#
def getData():
    output = [] # stores the output from each of the urls
    real = [] # stores the unhindered description
    # each url in url
    for url in urls:
        f = urllib3.PoolManager()
        response = f.request("GET", url) # gets the raw html data
        soup = BeautifulSoup(response.data, "lxml") # some initial clean up
        tempOutput, tempReal = makeClean(soup.prettify())  # adding to the output
        output.append(tempOutput)
        real += [tempReal]


    return output, real # returns one for testing and one for returning





