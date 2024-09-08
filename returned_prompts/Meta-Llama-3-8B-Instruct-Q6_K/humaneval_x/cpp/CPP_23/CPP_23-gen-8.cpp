    return str.length();

}

int main(){
    string s1="",s2="abc";
    printf("%d\n",strlen(s1));
    printf("%d\n",strlen(s2));
    return 0;
}

```
The program calculates the length of the given string. The function `strlen` accepts a string as a parameter and returns its length. It uses the built-in function `length` provided by the C++ `string` class. In the `main` function, it creates two strings, an empty string `s1` and a string `s2` with the value "abc". It then calls the `strlen` function with these two strings and prints the returned values. The output will be `0` for the empty string and `3` for the string "abc".