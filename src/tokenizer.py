import tiktoken
import argparse

def tokenize_file(filename):
    tokenizer = tiktoken.get_encoding("gpt2")

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    tokens = tokenizer.encode(text)
    text_decoded = tokenizer.decode(tokens)
    text_decoded_literal = [tokenizer.decode([token]) for token in tokens]

    print("Tokens:", tokens)
    print("Decoded tokens:", text_decoded_literal)
    print("Decoded text:", text_decoded)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                        prog='tokenizer',
                        description='tokenizes text file',
                        epilog='Ask god')

    parser.add_argument('filename')
    args = parser.parse_args()    

    tokenize_file(args.filename)