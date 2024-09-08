    int i;
    for(i=0;str[i];i++);
    return i;

}

int main() {
    string str;
    cin>>str;
    printf("Length of the string: %d\n",strlen(str));
    return 0;
}
```

**Explanation:**
The program is designed to calculate the length of a given string. The `strlen` function is implemented to achieve this. It iterates through the string using a for loop, counting the number of characters until it reaches the null character (`\0`) at the end of the string. The number of iterations is the length of the string, which is then returned by the function.

In the `main` function, a string is taken as input from the user using `cin`. The `strlen` function is then called with this string as an argument, and the result is printed to the console using `printf`.

**Example Output:**

```
Length of the string: 3
```

**Note:** The `strlen` function is not a standard C++ function. The standard C++ function to get the length of a string is `size()` or `length()`. The implementation above is a custom implementation of `strlen` for educational purposes. In a real-world scenario, you would use the standard library functions.