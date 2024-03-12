import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def main():
    nltk.download('punkt')
    text = input("Enter the text: ")   # text example : Hello Tarek Omar Gawish, how are you? I hope everything is goning well. Today is a good day, see you soon!

    print("\nChoose one of the following options:")
    print("1. Print tokenized words")
    print("2. Print tokenized sentences")
    print("3. Print output using split function")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        print_tokenized_words(text)
    elif choice == '2':
        print_tokenized_sentences(text)
    elif choice == '3':
        print_output_using_split(text)
    else:
        print("Invalid choice")

def print_tokenized_words(text):
    tokens = word_tokenize(text)
    print("Tokenized words:")
    print(tokens)

def print_tokenized_sentences(text):
    sentences = sent_tokenize(text)
    print("Tokenized sentences:")
    print(sentences)

def print_output_using_split(text):
    words = text.split()
    print("Output using split function:")
    print(words)

if __name__ == "__main__":
    main()



