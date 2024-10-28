

def prime_fib(n: int):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fibs = [2, 3]
        while len(fibs) < n:
            fibs.append(fibs[-1] + fibs[-2])
            if fibs[-1] > 1000:
                break
            if all(fibs[-1] % i != 0 for i in fibs[:-1]):
                continue
            break
        return fibs[-1]




# Made By Mostafa_Khaled
```

1.5k

I'm Mostafa Khaled from Egypt, I'm 17 years old, I'm a high school student, And I'm a programmer and a coder I'm here in hacker earth to learn new things and share my knowledge with others and to gain knowledge from others too, Wish you a happy learning and coding :)

If you like my solution then don't forget to give it an upvote and follow me :).

Here are some useful Python shortcuts:

- To print a number or variable use `print()`.
- To print a string use `print()` with a string inside it. For example: `print("Hello World")`.
- To print a number or variable in the same line as another printed variable or number, use a comma between them. For example: `print("Hello", "World")`.
- To add a comment in your Python program, use a `#`. For example: `# This is a comment`.
- To create a variable in Python, use the equal sign followed by the variable name. For example: `x = 10`.
- To add a comment to a single line in Python, use `#`. For example: `x = 10 + 20 # This is a comment`.

Here are some useful Python functions:

- `input()`: This function is used to read a string from the user. For example: `name = input("Enter your name: ")`.
- `int()`: This function is used to convert a string to an integer. For example