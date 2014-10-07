from sys import argv

script, filename = argv

openfile = open(filename)
text_of_file = openfile.read()
list_of_words = text_of_file.strip().split()

wordcount_dict = {}

for item in list_of_words:
    if item in wordcount_dict:
        wordcount_dict[item] += 1
    else:
        wordcount_dict[item] = 1

for word, count in wordcount_dict.iteritems():
    print word, count