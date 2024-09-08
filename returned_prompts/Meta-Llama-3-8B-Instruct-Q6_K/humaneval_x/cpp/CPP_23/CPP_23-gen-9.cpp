    int i = 0;
    while (str[i] != '\0') {
        i++;
    }
    return i;
}

int main() {
    string str;
    cin >> str;
    cout << "Length of string is: " << strlen(str) << endl;
    return 0;
}

Output:
Enter the string: abc
Length of string is: 3
Enter the string: 
Length of string is: 0

Explanation:
This program uses C++ language to find the length of a given string. The function `strlen` is used to find the length of the string by iterating over the string until it reaches the null character (`'\0'`) which marks the end of the string. The `main` function takes a string as input from the user and then calls the `strlen` function to find its length. The length is then printed on the console. In the first test case, the input string is "abc" and its length is 3. In the second test case, the input string is an empty string and its length is 0.  */





