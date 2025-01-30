from collections import deque

def is_palindrome(input_string):
    #  Remove the samples and lower the line
    cleaned_string = ''.join(input_string.split()).lower()

    # Check if the line is empty
    if not cleaned_string:
        print(f"The string is empty.")
        return False
    
    # Create a two-way queue and add all symbols
    char_deque = deque(cleaned_string)

    # Compare symbols from both ends of the queue
    while len(char_deque) > 1:
        # Check if the first and last symbols match
        if char_deque.popleft() != char_deque.pop():
            print(f"The string is NOT a palindrome.")
            return False 

    # If all symbols match    
    print(f"The string IS a palindrome.")
    return True 

if __name__ == "__main__":
    while True:
        input_string = input("Enter the line: ").strip()
        is_palindrome(input_string)
