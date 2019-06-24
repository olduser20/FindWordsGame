
import sys
import codecs,re,string

# Find words
# Initializing

dic_file='Persian-Spell-Checker/Moin_Key_Words'
# dic_file='Word_collection_1.txt'

dic_words = [line.strip().replace(', ', ',').split('\t') for line in codecs.open(dic_file, encoding='utf-8')]

# print(type(dic_words))

print(len(dic_words))

word=dic_words[0][0]
# print(word)
print(word[::-1])
# print(type(word[::-1]))
# print(dir(word)) 

# words=open('Persian-Spell-Checker/Moin_Key_Words', mode='r' ,encoding='utf-8')

# print(len(dic_words.readlines(100)))
# print(words.readlines())
# words=words

letter_list="ابلق"

# print(letter_list[0])
# Two words

for i in letter_list:
    for j in letter_list:
        temp_word=i+j
        # print(temp_word)
        # print(type(temp_word))
        print(temp_word in dic_words)
        if list(temp_word) in dic_words:
            # print(temp_word==di)
            print(temp_word)

# print(dic_words)

# print()

# contents=words.read().encode("utf-8") 

#contents=words.readline(1).encode("utf-8") 
# print(len(words.read(20)))

# print("سلام")