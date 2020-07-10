# text analysis
from utils import *

print("Analysing The Mysterious Affair at Styles by Agatha Christie.")
# chapter mappings
chapter_mapping = {
    1: "I GO TO STYLES",
    2: "THE 16TH AND 17TH OF JULY",
    3: "THE NIGHT OF THE TRAGEDY",
    4: "POIROT INVESTIGATES",
    5: "\"IT ISN'T STRYCHNINE, IS IT?\"",
    6: "THE INQUEST",
    7: "POIROT PAYS HIS DEBTS",
    8: "FRESH SUSPICIONS",
    9: "DR. BAUERSTEIN",
    10: "THE ARREST",
    11: "THE CASE FOR THE PROSECUTION",
    12: "THE LAST LINK",
    13: "POIROT EXPLAINS"
}

num_words = getTotalNumberOfWords("863.txt")
print(f"There are {num_words} words in this text.")

num_unique_words = getTotalUniqueWords("863.txt")
print(f"There are {num_unique_words} unique words in this text.")

top_20_words = get20MostFrequentWords("863.txt")
print("The top 20 unique words are\n", top_20_words)

top_20_interesting_words = get20MostInterestingFrequentWords("863.txt")
print("The top 20 interesting unique words are\n", top_20_interesting_words)

bottom_20_interesting_words = get20LeastFrequentWords("863.txt")
print("20 least used interesting unique words are\n", bottom_20_interesting_words)

poirot_dist = getFrequencyOfWord("poirot")
print("Frequency of use of Poirot in each chapter is", poirot_dist)

quote = "A man in love is a sorry spectacle."
chapter_quote_found = getChapterQuoteAppears(quote)
print("The quote \"", quote, "\" was found in chapter", chapter_quote_found)
