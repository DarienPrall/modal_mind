import nltk
from nltk.corpus import gutenberg

#nltk.download('gutenberg')
#nltk.download('punkt')

#Get all the files in gutenberg so I can open each file
text_files = gutenberg.fileids()

# Creating a list of modals to check against
list_of_modals = ['can', 'could', 'may', 'might', 'will', 'would', 'should']

frequency_of_modals = {}

#for text_file in all_texts:
#    print(text_file)

# Go through every text_file
for text in text_files:
    # Generate an array of the text_files title and words
    words = gutenberg.words(text)
    modal_counts_dictionary = {}
    for modal in list_of_modals:
        modal_counts_dictionary[modal] = words.count(modal)
    frequency_of_modals[text] = modal_counts_dictionary

for text, counts in frequency_of_modals.items():
    print(f"Text: {text}")
    for modal, count in counts.items():
        print(f"{modal}:{count}")



