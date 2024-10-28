    int count = 0;
    string vowels = "aeiou";
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    for(int i = 0; i < s.size(); i++){
        if(vowels.find(s[i]) != string::npos){
            count++;
        }
    }
    if(s[s.size()-1] == 'y'){
        count++;
    }
    return count;
}


int main() {
    string s;
    printf("Enter the word: ");
    getline(cin, s);
    printf("Count of vowels: %d", vowels_count(s));
    return 0;
}
```

Here, we first initialize a count variable to zero. We then define a string vowels which contains all the vowels. We convert the input string to lowercase using the transform function. 

Next, we iterate over each character in the string. If the character is a vowel (i.e., if it is found in the string vowels), we increment the count. 

Finally, we check if the last character in the string is 'y'. If it is, we increment the count. We then return the count.

This solution assumes that the input string only contains alphabetical characters and does not contain any special characters or numbers. If the input string can contain uppercase letters, then we should replace the line `transform(s.begin(), s.end(), s.begin(), ::tolower);` with `s = to_lower(s);` where `to_lower` is a function that converts a string to lowercase.

Also, this solution does not handle words with capitalized vowels, as 'A', 'E', 'I', 'O', 'U' are not considered as vowels.

If you want to consider 'y' as a vowel even if it is uppercase, then you can simply add 'Y' to the string vowels.

Note: This program is written in C++.








































