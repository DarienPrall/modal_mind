#----------------------------------------------------------------------
#
# PROJECT INFORMATION
# Title: ModalMind
# Author: Darien Prall
# Start Date: 01-04-2025 (mmddyyyy)
# End Date: 
# Project Description: For this project, I explore the usage of modal verbs in different texts from the Gutenberg Corpus. I will analyze the relative frequency through different Natural Language Processing (NLP) techniques.
#
# PROJECT STEPS
# Task 0: Import and Clean Data
#
# Task 1: Modals in the Gutenberg Corpus
# - Task 1.1: Install NLTK
# - Task 1.2: Download the Gutenberg Corpus
# - Task 1.3: Define Each Modal Group
# - Task 1.4: Count Relative Frequencies of Each Modal Verb
# - Task 1.5: Find the Texts with the Largest Span of Modal Frequencies
# - Task 1.6: Compare Usage of Modals in the Two Texts
#
# Task 2: Inaugural Corpus - Analyzing Kennedy's 1961 Speech
# - Task 2.1: Download the Inaugural Corpus
# - Task 2.2: Load the 1961 Kennedy Speech
# - Task 2.3: Identify the 10 Most Frequent Used Long Words
# - Task 2.4: Use WordNet to Find Synonyms and Hyponyms
# - Task 2.5: Reflect of the Results
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# Task 1: Modals in the Gutenberg Corpus

# - Task 1.1: Install NLTK
# What this code is doing: Importing the NLTK library to allow the download of the gutenberg texts
import nltk
from nltk.corpus import gutenberg

# - Task 1.2: Download the Gutenberg Corpus
# What this code is doing: Downloading the gutenberg texts and splitter. Storing all texts to a variable to print what they are
#nltk.download('gutenberg')
#nltk.download('punkt')

texts = gutenberg.fileids()
# checking each file
for text in texts:
    print(text)

# - Task 1.3: Define Each Modal Group
# What this code is doing: Creating a list of modal verbs I wnat to look for within the texts
list_of_modals = ['can', 'could', 'may', 'might', 'will', 'would', 'should']

# - Task 1.4: Count Relative Frequencies of Each Modal Verb
# What this code is doing: Creating a dictionary to store the modals and their counts. Then, I need to loop through each file in the gutenberg tests, looking for each modal verb and counting them
frequency_of_modals = {}
for text in texts:
    words = gutenberg.words(text)
    #print(words)
    count_modal = {}
    for modal in list_of_modals:
        count_modal[modal] = words.count(modal)
    frequency_of_modals[text] = count_modal

for text, counts in frequency_of_modals.items():
    print(f"Text: {text}")
    for modal, count in counts.items():
        print(f"{modal}: {count}\n")

# - Task 1.5: Find the Texts with the Largest Span of Modal Frequencies
# What this code is doing:
#

# - Task 1.6: Compare Usage of Modals in the Two Texts
# What this code is doing:
#

#----------------------------------------------------------------------

#----------------------------------------------------------------------
# Task 2: Inaugural Corpus - Analyzing Kennedy's 1961 Speech

# - Task 2.1: Download the Inaugural Corpus
# What this code is doing:
#

# - Task 2.2: Load the 1961 Kennedy Speech
# What this code is doing:
#

# - Task 2.3: Identify the 10 Most Frequent Used Long Words
# What this code is doing:
#

# - Task 2.4: Use WordNet to Find Synonyms and Hyponyms
# What this code is doing:
#

# - Task 2.5: Reflect of the Results
# What this code is doing:
#
#----------------------------------------------------------------------