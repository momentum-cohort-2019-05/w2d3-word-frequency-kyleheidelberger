def print_word_freq(file):

    # open file
    with open(file) as file:
        # convert file to string
        string = file.read()

        # remove punctuation and capitals; fix spacing
        import re
        string = string.strip()
        string = re.sub(r'[^A-Za-z" "\n]', "", string)
        string = string.replace("\n", " ")
        string = string.lower()

        # split string into list
        words = string.split(" ")

        # words to ignore when checking for frequency
        STOP_WORDS = [
            'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
            'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
            'will', 'with'
        ]

        # create dictionary
        word_dictionary = {}
        for word in words:
                if not word in STOP_WORDS and word != "":
                    if word_dictionary.get(word) == None:
                        word_dictionary[word] = 1
                    else:
                        word_dictionary[word] += 1
        
        # sort words alphabetically and convert to tuples
        def sort_words(word_tuples):
            return word_tuples[0]
        
        alphabetic_words = sorted(word_dictionary.items(), key=sort_words)

        # sort tuples by word frequency and limit to 10 most frequent
        def sort_frequency(word_tuples):
            return word_tuples[1]

        most_frequent = sorted(alphabetic_words, key=sort_frequency, reverse=True)[:10]
        
        # prints the results
    # print(most_frequent)
        


        



# identifies valid file to run - don't mess with this!
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
