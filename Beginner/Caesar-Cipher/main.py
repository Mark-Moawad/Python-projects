import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(text, shift):
  
#   # converting the string to a list to manipulate easily
#   text_as_list = []
#   for i in range(len(text)):
#     text_as_list.append(text[i])
    
#   # checking if the character is a letter of the alphabet, not a symbol
#   # and shifts the character the required shift amount
#   for char in range(len(text_as_list)):
#     current_letter = text_as_list[char]
#     if current_letter in alphabet:
#       list_index = alphabet.index(current_letter) + shift
#       if list_index > len(alphabet) - 1:
#         # We have two ways to tackle the problem of going out of list index
#         # bounds, first way:
#         # list_index = (len(alphabet) - list_index) * -1
#         # second way:
#         list_index = list_index % len(alphabet)
#       text_as_list[char] = alphabet[list_index]
  
#   # converting the text list back to string
#   text = ""
#   for j in range(len(text_as_list)):
#     text += text_as_list[j]
#   print(text)

# def decrypt(text, shift):

#   # converting the string to a list to manipulate easily
#   text_as_list = []
#   for i in range(len(text)):
#     text_as_list.append(text[i])
    
#   # checking if the character is a letter of the alphabet, not a symbol
#   # and shifts the character the required shift amount
#   for char in range(len(text_as_list)):
#     current_letter = text_as_list[char]
#     if current_letter in alphabet:
#       list_index = (alphabet.index(current_letter) - shift) % len(alphabet)
#       text_as_list[char] = alphabet[list_index]
  
#   # converting the text list back to string
#   text = ""
#   for j in range(len(text_as_list)):
#     text += text_as_list[j]
#   print(text)

# if direction == 'encode':
#   encrypt(text, shift)
# elif direction == 'decode':
#   decrypt(text, shift)
# else:
#   print("Invalid input!")

def caesar(text, shift, direction):
  output_text = ""
  if shift > len(alphabet):
    shift %= len(alphabet)
  if direction == "decode":
      shift *= -1
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      output_text += alphabet[new_position]
    else:
      output_text += char
    
  print(f"Here's the {direction}d result: {output_text}")
  
should_end = False
while not should_end:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye!")