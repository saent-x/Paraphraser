# Author: Vangerwua Johnpaul ✌
# This is a simple tool that can be used to paraphrase a simple sentence (Still a work in progress though)

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# First Step: Tokenize the sentence into an array of words
# Second Step: Find the synonyms of these words using the nltk library
# Third Step: Reconstruct the sentence and then print it out to the console

words_not_to_be_changed = ["or", "is", "of", "for", "this",
                           "and", "am", "a", "that", "in", "at", "there", "that", "are"]


def check_staticwords(token):
    if (words_not_to_be_changed.count(token.lower()) > 0 or token.isupper()):
        return False
    return True


def Paraphrase(array):
    newTokenArray = []
    tempArray = []

    for token in array:
        if (check_staticwords(token)):
            data = wordnet.synsets(token)
            for synonym in data:
                for lemma in synonym.lemmas():
                    if (lemma.name().lower() != token.lower()):
                        tempArray.append(lemma.name())

        if len(tempArray) > 0:
            # pick the first item
            newTokenArray.append(tempArray[0])
            tempArray.clear()
        else:
            newTokenArray.append(token)

    return newTokenArray

# By the way words that dont not make sense when re-phrased should be bolded (not really sophisticated)

test_sentence1 = "Today is a good day"
test_sentence2 = "Kindly NOTE that NIMC will never ask you to upload your BVN or NIN on any PORTAL"
test_sentence3 = "There AI are disasters in the world"
test_sentence4 = "If only there were one religion"
test_sentence5 = "I think this paraphrasing tool is really cool"

# The test sentences can be substituted to yield different results
tokens = word_tokenize(test_sentence5)

result = Paraphrase(tokens)
print(result)
