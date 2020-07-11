#!/usr/bin/python3

# text analysis
from utils import *

filename = input("Enter the name of the file to analyse: ")
print("Analysing " + filename)


num_words = getTotalNumberOfWords(filename)
print(f"There are {num_words} words in this text.")

num_unique_words = getTotalUniqueWords(filename)
print(f"There are {num_unique_words} unique words in this text.")

top_20_words = get20MostFrequentWords(filename)
print("The top 20 unique words are\n", top_20_words)

top_20_interesting_words = get20MostInterestingFrequentWords(filename)
print("The top 20 interesting unique words are\n", top_20_interesting_words)

bottom_20_interesting_words = get20LeastFrequentWords(filename)
print("20 least used interesting unique words are\n", bottom_20_interesting_words)

to_search = input("Do you want to track the progression of a word over chapters? [y/n] ")
if to_search in ["y", "Y", "yes"]:
    word_to_search = input("Enter the word to search: ")
    word_dist = getFrequencyOfWord(word_to_search, filename)
    print("Frequency of use of " + word_to_search + " in each chapter is", word_dist)

to_search_quote = input("Do you want to search for a quote? [y/n] ")
if to_search_quote in ["y", "Y", "yes"]:
    quote = input("Enter quote to search: ")
    chapter_quote_found = getChapterQuoteAppears(quote, filename)
    print("The quote \"", quote, "\" was found in chapter", chapter_quote_found)

generated_sentence = generateSentence(filename)
print("A randomly generated sentence using unigrams starting with \"The\" is:\n", generated_sentence)
