# words to ignore when checking for frequency
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]



# open file
file = open("seneca_falls.txt")
# convert file to string
string = file.read()

print(string)

# remove punctuation and capitals; fix spacing
import re
string = re.sub(r'[^A-Za-z." "\n]', "", string)
string = string.replace("\n", " ")
string = string.lower()

print(string)

# split string
words = string.split(" ")

# print  as a test
print(words)

# calculate word frequency
def print_word_freq(words):
    """Read in `file` and print out the frequency of words in that file."""
    pass
   



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
