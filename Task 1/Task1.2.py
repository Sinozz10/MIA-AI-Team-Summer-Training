'''This is Task 1.2 of MIA Summer training for AI SUB-TEAM
Program created and programmed by: Yassin Khaled, CCE28
Required to do :
1. Implement the encode and decode. Done
2. Your encoding method must work for any possible string, including empty strings or strings containing numbers and special characters. Done
3. Your script should demonstrate that your code works by:
○ Creating a list of sample F1 commands. Done
○ Encoding the list and printing the single string. Done
○ Decoding that string and printing the resulting list to match the original. Done
'''
class coding:
    def __init__(self):
        self.original_list = []
        
    def encoded_string(self, *args): # This encodes the input by reversing each word
        self.original_list = list(args)
        return ''.join(word[::-1] for word in args)#This will reverse each word and concatenate them into a single string

    def decoded_string(self, encoded_str, word_lengths): # This decodes the string back to the original list
        original_list = []
        start = 0
        for length in word_lengths:
            original_list.append(encoded_str[start:start + length][::-1])
            start += length
        return original_list

user_input = input("Enter a list of commands (Quotes for each word ,with commas in between): ")
print(f'Input: [{user_input}]') #test
if user_input == "" or user_input.isspace(): # Check if input is empty or contains only whitespace
    print("Output: []")  # If input is empty, output an empty list
    exit()  # Exit the program if input is empty
else:
    command_list = [item.strip('"') for item in user_input.split('", "')]#I added this to fix "Box,Box" issue
    object = coding()
    encoded_list= object.encoded_string(*command_list) #This will encode the input by reversing each word
    # print(f'Encoded string: {encoded_list}') this was tested to check the encoded string correctly
    word_lengths = [len(word) for word in command_list] #This was a must to my approach as the decode function requires the word lengths
    decoded_list = object.decoded_string(encoded_list, word_lengths)
    print(f'Output: {decoded_list}')# This will print the original list of commands again after decoding