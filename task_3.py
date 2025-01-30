def check_brackets(input_string):
    stack = []
    
    # Define pairs of opening and closing parentheses
    matching_brackets = {')': '(', '}': '{', ']': '['}

    if not input_string:
        print(f"Empty string")
        return
    
    for char in input_string:
        # Check if the character is an opening bracket
        if char in matching_brackets.values(): 
            stack.append(char)
        # Check if the character is a closing bracket
        elif char in matching_brackets.keys():  
            if stack and stack[-1] == matching_brackets[char]:
                # Remove a pair if they are correct
                stack.pop()  
            else:
                print(f"Asymmetrical")
                return
    
    if not stack:
        print(f"Symmetrically")
    else:
        print(f"Asymmetrical")

if __name__ == "__main__":
    while True:
        input_string = input("Enter a string with parentheses: ").strip()
        check_brackets(input_string)
