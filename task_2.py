from collections import deque

def is_palindrome(input_string):
    #  Remove the samples and lower the line
    cleaned_string = ''.join(input_string.split()).lower()
    
    # Create a two-way queue and add all symbols
    char_deque = deque(cleaned_string)
    
    # Compare symbols from both ends of the queue
    while len(char_deque) > 1:
        # Check if the first and last symbols match
        if char_deque.popleft() != char_deque.pop():
            print(f"The string is not a palindrome.")
            return False 

    # If all symbols match    
    print(f"The string is a palindrome.")
    return True 

while True:
    input_string = input("Enter the line: ").strip()
    is_palindrome(input_string)
