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
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
    counter = collections.Counter(word_dict)
    top_words = []
    for key, value in counter.most_common(20):
        top_words.append([key, value])
    return top_words
