    if (s.length()<3) {
        return false;
    }
    else {
        for (int i=0; i<s.length()-2; i++) {
            if (s[i]==s[i+1] || s[i+1]==s[i+2] || s[i]==s[i+2]) {
                return false;
            }
        }
    }
    return true;
}
int main() {
    string s;
    printf("Enter a string: ");
    cin >> s;
    if (is_happy(s) == true) {
        printf("The string is happy\n");
    }
    else {
        printf("The string is not happy\n");
    }
    return 0;
}
```

The program works by iterating through the string and checking if three consecutive characters are the same. If they are, the function returns false. If the loop completes without finding any such instances, the function returns true, indicating that the string is happy.

For example, the string "adb" is happy because 'a' is not equal to 'd' and 'd' is not equal to 'b'. Similarly, "xyy" is not happy because 'y' is equal to 'y'.

The program uses the `cin` function to get the string from the user, and then uses the `is_happy` function to check if the string is happy. It then prints the result.


```

```







































































































































































