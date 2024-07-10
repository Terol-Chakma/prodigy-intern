def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift * direction) % 26 + ascii_offset)
        else:
            result += char
    return result
text = input("Enter your message: ")
shift = int(input("Enter the shift value: "))
encrypted_text = caesar_cipher(text, shift, 1)
decrypted_text = caesar_cipher(encrypted_text, shift, -1)
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")