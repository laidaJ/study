import string
alphabet = list(string.ascii_lowercase) + list(string.ascii_lowercase) 
print(alphabet)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here is the {cipher_direction}d code : {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    start_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if start_again == "no":
        should_continue = False
        print("Good bye")
