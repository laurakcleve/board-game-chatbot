import tiktoken

TOKEN_ENCODING = "p50k_base"
# TOKEN_ENCODING = "cl100k_base"

TEXT = "Note: In the first turn of the game, do not pass the First Player token.  Each time players are required to do anything in order, start with the player with the First Player token, and then continue with each player in clockwise order."
# TEXT = "Sample text for token example"


if __name__ == "__main__":

    encoding = tiktoken.get_encoding(TOKEN_ENCODING)
    tokens = encoding.encode(TEXT)
    byte_strings = [encoding.decode_single_token_bytes(
        token) for token in tokens]
    strings = [byte_string.decode('utf-8') for byte_string in byte_strings]
    print(strings)
