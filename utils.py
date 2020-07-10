import collections

# a collection of helper functions to use


def readFile(filename):
    '''takes in a file with name filename and returns list of lines read, unprocessed'''
    with open(filename, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def getTotalNumberOfWords(filename):
    '''takes in a file with name filename and returns the total number of words in the file'''
    word_count = 0
    lines = readFile(filename)
    for line in lines:
        if line[:7] != "CHAPTER":
            word_count += len(line.split())
    return word_count


def getTotalUniqueWords(filename):
    '''takes in a file with name filename and returns the number of unique words in the file'''
    unique_words = set()
    lines = readFile(filename)
    for line in lines:
        if line[:7] != "CHAPTER":
            words = line.split()
            for word in words:
                unique_words.add(word)
    return len(unique_words)


def get20MostFrequentWords(filename):
    '''takes in a file with name filename and returns an array of the top 20 words in the file along with their counts'''
    lines = readFile(filename)
    word_dict = {}
    for line in lines:
        if line[:7] != "CHAPTER":
            words = line.split()
            for word in words:
                word = word.strip(" ,\".:\'").lower()
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
    counter = collections.Counter(word_dict)
    top_words = []
    for key, value in counter.most_common(20):
        top_words.append([key, value])
    return top_words


def get20MostInterestingFrequentWords(filename):
    '''takes in a file with name filename and returns an array of the top 20 interesting words in the file along with their counts'''
    lines = readFile(filename)
    stopwords_list = readFile("1-1000.txt")
    stopwords = [i.strip().lower() for i in stopwords_list]
    stopwords = set(stopwords)
    word_dict = {}
    for line in lines:
        if line[:7] != "CHAPTER":
            words = line.split()
            for word in words:
                word = word.strip(" ,\".:\'").lower()
                if word in stopwords:
                    continue
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
    counter = collections.Counter(word_dict)
    top_words = []
    for key, value in counter.most_common(20):
        top_words.append([key, value])
    return top_words


def get20LeastFrequentWords(filename):
    '''takes in a file with name filename and returns an array of the 20 least frequent interesting words in the file along with their counts'''
    lines = readFile(filename)
    stopwords_list = readFile("1-1000.txt")
    stopwords = [i.strip().lower() for i in stopwords_list]
    stopwords = set(stopwords)
    word_dict = {}
    for line in lines:
        if line[:7] != "CHAPTER":
            words = line.split()
            for word in words:
                word = word.strip(" ,\".:\'").lower()
                if word in stopwords:
                    continue
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
    least_frequent_words = []
    # assumes >= 20 words are used only once
    for key, value in word_dict.items():
        if value == 1:
            least_frequent_words.append([key, value])
        if len(least_frequent_words) == 20:
            break
    return least_frequent_words


def getFrequencyOfWord(given_word):
    '''take in a word and return an array of the number of the times the word was used in each chapter'''
    lines = readFile("863.txt")
    given_word = given_word.lower()
    frequency_array = []
    count = 0
    for line in lines:
        if line[:7] != "CHAPTER":
            words = line.split()
            for word in words:
                word = word.strip(" ,\".:\'").lower()
                if word == given_word:
                    count += 1
        else:
            frequency_array.append(count)
            count = 0
    return frequency_array
