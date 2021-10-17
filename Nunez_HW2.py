#1
zen = "Beautiful is better than ugly. \n" \
"Explicit is better than implicit. \n" \
"Simple is better than complex."

zen = zen.replace('.', "")

word_count = [len(word) for word in zen.split()]
print("#Q1\n",word_count,"\n")

#2
zen = "Beautiful is better than ugly. \n" \
"Explicit is better than implicit. \n" \
"Simple is better than complex."

punctuation = "!?;"
for punc in punctuation:
    zen = zen.replace(punc,"")
words_in_sentences = [sentence.split() for sentence in zen.split('.') if sentence]
print(words_in_sentences,"\n")

#3
num_words_in_sent = [len(sentence) for sentence in words_in_sentences]
print(num_words_in_sent)

#4
zen = "Beautiful is better than ugly. \n" \
"Explicit is better than implicit. \n" \
"Simple is better than complex."
zen = zen.replace('.', "")
wordList = [word for word in zen.split()] 
word_count = [len(word) for word in zen.split()]                           
myDict = { k:v for (k,v) in zip(wordList, word_count)}  
print(myDict)       

# =============================================================================
# or....
# newdict =dict();
# for i in range(len(word_count)):
#     newdict[wordList[i]]=word_count[i]
# print(newdict)
# =============================================================================

    