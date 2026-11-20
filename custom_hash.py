def custom_hash(text):
    hash_value = 0

    for index, char in enumerate(text):
        numeric = ord(char)
        total = numeric * (index + 1)
        hash_value += total

    return hash_value
    
    
def compare_hashes(text1, text2):

    # TODO 1:
    # Calculate the hash of text1
    hash1 = custom_hash(text1)
    # TODO 2:
    # Calculate the hash of text2
    hash2 = custom_hash(text2)
    # TODO 3:
    # Compare both hash values
    compare = hash1 == hash2
    # TODO 4:
    # Return True if equal, False otherwise
    if compare:
        return True
    
    return False

if __name__ == "__main__":
    print(custom_hash("ABC"))
    print(custom_hash("CBA"))

    print(compare_hashes("ABC", "ABC"))
    print(compare_hashes("ABC", "CBA"))