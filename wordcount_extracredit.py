from sys import argv
import string

script, filename = argv

openfile = open(filename)
text_of_file = openfile.read()
text_of_file = text_of_file.strip().lower()

clean_string = ''

for char in text_of_file:
    if char not in string.punctuation:
        clean_string += char

list_of_words = clean_string.split() #the above removed punctuation and made all words lowercase

wordcount_dict = {}

for item in list_of_words:
    if item in wordcount_dict:
        wordcount_dict[item] += 1
    else:
        wordcount_dict[item] = 1


print 'Here are the words and word counts sorted by word count in decreasing order.'

sorted_count = sorted(wordcount_dict.values())
sorted_word = sorted(wordcount_dict, key=wordcount_dict.get)

sorted_count = sorted_count[::-1]
sorted_word = sorted_word[::-1]

for item in sorted_word:
    print 'the word "%s" is mentioned %s times' % (item, sorted_count[sorted_word.index(item)])

print '*' * 10

tuple_version = [(wordcount, word) for word, wordcount in wordcount_dict.iteritems()]
tuple_version = sorted(tuple_version)

print 'Here are the words and word counts sorted alphabetically by word count.'

for item in tuple_version:
    print 'The word %s is mentioned %s times' % (item[1], item[0])


