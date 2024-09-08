return str.length();

}
int main(){
    string s;
    cin>>s;
    cout<<"Length of given string is : "<<strlen(s)<<endl;
    return 0;
}
```
This C++ program calculates and prints the length of a given string. The length of a string is the number of characters it contains. The program uses the `std::string` class and its `length()` method to calculate the length of the string.

Here's how the program works:
1. The program includes the necessary headers (`<stdio.h>` and `<string>`) and uses the `using namespace std;` directive to avoid having to prefix standard library elements with `std::`.
2. The `strlen` function is defined to take a `std::string` object as its argument and return an `int` value representing the length of the string.
3. In the `main` function, the program reads a string from the standard input using `cin`.
4. The program calls the `strlen` function with the input string as its argument and prints the result to the standard output using `cout`.
5. The program returns 0 to indicate successful execution.

The output of the program will be the length of the input string. For example, if the input string is "abc", the output will be "3". If the input string is an empty string, the output will be "0". 

Note: The `strlen` function is a common function in C programming, but in C++, it's not necessary to define your own `strlen` function, as the `std::string` class provides a `length()` method that does the same thing. The program above is simply an example of how to define and use a custom `strlen` function in C++. In a real-world program, you would typically use the `std::string` class and its methods instead of defining your own custom functions.