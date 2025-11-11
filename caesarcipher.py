alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dictionary = input("Enter the text to be encode/decode: ").lower()
text = input("Type your message:")
shift = int(input("Type the shift number:"))

def encrypt(original_text,shift_amount) :
    cipher_text = ""
    for letter in original_text :
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet) # fix for we choose z as letter
        cipher_text += alphabet[shifted_position]
    print(f"The encoded text is {cipher_text}")

def decrypt(original_text,shift_amount) :
    decipher_text = ""
    for letter in original_text :
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet) # fix for we choose a as letter
        decipher_text += alphabet[shifted_position]
    print(f"The decoded text is {decipher_text}")

def caesar(original_text,shift_amount,operation) :
    if operation == "encode" :
        encrypt(original_text,shift_amount)
    elif operation == "decode" :
        decrypt(original_text,shift_amount)
    else :
        print("Invalid operation. Please choose 'encode' or 'decode'.")
        
caesar(original_text=text,shift_amount=shift,operation=dictionary)

restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
if restart == "yes" :
    caesar(original_text=text,shift_amount=shift,operation=dictionary)
else :
    print("Goodbye!")