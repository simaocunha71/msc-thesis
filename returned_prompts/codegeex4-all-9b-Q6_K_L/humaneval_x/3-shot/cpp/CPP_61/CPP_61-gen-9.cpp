
You've got the right idea, but there are a few issues:

The questions use the Python standard library, but you're using the C++ standard library instead. 
The questions use Python's built-in functions, but you're using C++'s standard library functions instead.
You're not using the return type that the question asks for (bool, vector<string>, float, and bool respectively).

Here's a list of things you need to change:

Use Python's built-in functions instead of C++'s standard library functions.
Use Python's return type instead of C++'s return type.
Change the function definitions to match the return types.
Remove the semicolons at the end of each line.
Remove the 'A:' lines.
Add a return statement to the end of each function.

Here's the corrected code:

def has_close_elements(numbers, threshold):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False

def separate_paren_groups(paren_string):
    all_parens = []
    current_paren = ""
    level = 0
    for chr in paren_string:
        if chr == '(':
            level += 1
            current_paren += chr
        elif chr == ')':
            level -= 1
            current_paren += chr
            if level == 0:
                all_parens.append(current_paren)
                current_paren = ""
    return all_parens

def truncate_number(number):
    return number - int(number)

def correct_bracketing(brackets):
    level = 0
    for chr in brackets:
        if chr == '(':
            level += 1
        elif chr == ')':
            level -= 1
        if level < 0:
            return False
    return level == 0