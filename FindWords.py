
import sys
import codecs,re,string


### Recursive Approach ###
def find_word_rec(lstWord):
    return 1



# Find words
# Initializing

dic_file='Moin_Key_Words.txt'
# dic_file='Word_collection_1.txt'

dic_words = [line.strip().replace(', ', ',').split('\t') for line in codecs.open(dic_file, encoding='utf-8')]


print("This is a test for collaboration!")


# print(type(dic_words))

# print(len(dic_words))

# word=dic_words[0][0]
# print(word)
# print(word[::-1])
# print(type(word[::-1]))
# print(dir(word))

# words=open('Persian-Spell-Checker/Moin_Key_Words', mode='r' ,encoding='utf-8')

# print(len(dic_words.readlines(100)))
# print(words.readlines())
# words=words

letter_list="اپتذرزی"

# print(letter_list[0])
# Two words

two_letter_words=[]
three_letter_words=[]
four_letter_words=[]
five_letter_words=[]
six_letter_words=[]
seven_letter_words=[]



count = 0

for i in letter_list:
    # Words with 2 letters
    for j in letter_list:
        temp_word=i+j
        list_temp_word=[temp_word[::-1]]
        if list_temp_word in dic_words[::]:
            two_letter_words.append(temp_word)
            # print(temp_word)
            count+=1
        
        # Words with 3 letters
        for k in letter_list:
            temp_word=i+j+k
            list_temp_word=[temp_word[::-1]]
            if list_temp_word in dic_words[::]:
                three_letter_words.append(temp_word)
                # print(temp_word)
                count+=1

        #     # Words with 4 letters
            for l in letter_list:
                temp_word=i+j+k+l
                list_temp_word=[temp_word[::-1]]
                if list_temp_word in dic_words[::]:
                    four_letter_words.append(temp_word)
                    # print(temp_word)
                    count+=1

        #         # Words with 5 letters
                for m in letter_list:
                    temp_word=i+j+k+l+m
                    list_temp_word=[temp_word[::-1]]
                    if list_temp_word in dic_words[::]:
                        five_letter_words.append(temp_word)
                        # print(temp_word)
                        count+=1

        #             # Words with 6 letters
        #             for n in letter_list:
        #                 temp_word=i+j+k+l+m+n
        #                 list_temp_word=[temp_word[::-1]]
        #                 if list_temp_word in dic_words[::]:
        #                     print(temp_word)
        #                     count+=1


        #                 # Words with 7 letters
        #                 for o in letter_list:
        #                     temp_word=i+j+k+l+m+o
        #                     list_temp_word=[temp_word[::-1]]
        #                     if list_temp_word in dic_words[::]:
        #                         print(temp_word)
        #                         count+=1


print("{0} words have been found!".format(count))
        
print("Two letter words are:")
print(two_letter_words)
print("\n")


print("Three letter words are:")
print(three_letter_words)
print("\n")


print("Four letter words are:")
print(four_letter_words)
print("\n")

print("Five letter words are:")
print(five_letter_words)
print("\n")

# print(dic_words)

# print()

# contents=words.read().encode("utf-8")

#contents=words.readline(1).encode("utf-8")
# print(len(words.read(20)))

# print(dic_words[:100])

# print("سلام"[::-1])