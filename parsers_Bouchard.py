################################################################################


#Collaberation with myself, Justin, Harold, Steven, and Zach 

# PART #1
################################################################################
import string
import os
from os import listdir
import csv
import json

def countWordsUnstructured(filename):
    wordcounts={}
    file = open(filename, encoding = 'utf-8')
    for word in file.read().split():
        for mark in string.punctuation:
            word = word.replace(mark, "")
        word = word.encode('utf-8')
        if word in wordcounts:
            wordcounts[word] = wordcounts[word]+1
        else:
            wordcounts[word] = 1
    return wordcounts
        #file.close();

wrd_dict= countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Trump_2017.txt')

    
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
    

################################################################################
# PART 2
################################################################################
    

def generateSimpleCSV(targetfile, wordCounts):    
    
    file = open(targetfile, "w")
    file.write("Word, Count\n")
    for word in wordCounts:
        count = wordCounts[word]
        file.write(str(word) + "," + str(count) + "\n")
    return 
   

generateSimpleCSV('targetfile.csv', wrd_dict) 

    # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting: 
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data
    
# Test your part 2 code below
    
################################################################################
# PART 3
################################################################################
def countWordsMany(directory): 
    #csvFile = open(target, 'w')
    #fileWriter = csv.writer(csvFile)
    #fileWeiter.writerow(['Word', 'Count'])
    #for word in wordCounts: 
    
    dir_list = os.listdir(directory)
    wordCountDict = {}
    for file in dir_list:
        listWordCount = countWordsUnstructured(directory + "/" + file)
        wordCountDict[file] = listWordCount
    return wordCountDict

master_dict = countWordsMany('./state-of-the-union-corpus-1989-2017')
#print(master_dict)

    # This function should create a dictionary of word count dictionaries
    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each
    # text file in the directory
    
# Test your part 3 code below"""

################################################################################
# PART 4
################################################################################
def generateDirectoryCSV(wordCounts, targetfile): 
    CSVfile=open(targetfile, 'w')
    CSVfile.write("filename, Word, Count\n")
    for wordfile, dict in wordCounts.items():
        for word, count in dict.items():
            CSVfile.write(wordfile + "," + str(word) + "," +str(count) + "\n")
        CSVfile.close()
        return 
generateDirectoryCSV(master_dict, "targetfile2.csv")
    
    
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header: 
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    
# Test your part 4 code below
    
################################################################################
# PART 5
################################################################################
def generateJSONFile(wordCounts, targetfile):
    JSONfile=open(targetfile, "w")
    JSONfile.write(str(wordCounts).replace("\'", "\""))
    JSONfile.close()
    return JSONfile
generateJSONFile(master_dict, "targetfile.json")
    # This function should create an containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files. 
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data
    
# Test your part 5 code below


################################################################################
# PART 6
################################################################################
#def searchCSV(csvfile, word): 
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
#def searchJSON(JSONfile, word): 
    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
# Test your part 6 code to find which file has the highest count of a given word

# +1 bonus point for figuring out how many datapoints you had to process to 
# compute this value