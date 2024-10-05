    from typing import List

    def separate_paren_groups(paren_string: str) -> List[str]:
        # Remove spaces from the input string
        paren_string = paren_string.replace(" ", "")

        # Initialize an empty list to store the groups
        groups = []

        # Initialize an empty string to build the current group
        current_group = ""

        # Iterate over the characters in the input string
        for char in paren_string:
            # If the character is an opening parenthesis, add it to the current group
            if char == "(":
                current_group += char
            # If the character is a closing parenthesis, add it to the current group if it's not empty
            elif char == ")":
                if current_group:
                    current_group += char
                    groups.append(current_group)
                    current_group = ""
                else:
                    current_group += char

        return groups

    # Test the function
    print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']



