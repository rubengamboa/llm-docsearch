import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")

text = "Hello, world!"
tokens = tokenizer.encode(text)
text_decoded = tokenizer.decode(tokens)
text_decoded_literal = [ tokenizer.decode([token]) for token in tokens ]
print("Tokens:", tokens)
print("Decoded tokens:", text_decoded_literal)
print("Decoded text:", text_decoded)
