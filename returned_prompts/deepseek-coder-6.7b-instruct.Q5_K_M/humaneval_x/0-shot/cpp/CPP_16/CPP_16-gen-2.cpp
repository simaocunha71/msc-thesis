    vector<int> count(256, 0);
    int distinct_count = 0;

B:
    for (int i=0; i<str.size(); i++){
        if (count[tolower(str[i])] == 0){
            distinct_count++;
        }
        count[tolower(str[i])]++;
    }

C:
    return distinct_count;
}

int main() {
    string str;
    printf("Enter a string: ");
    getline(cin, str);
    int result = count_distinct_characters(str);
    printf("The number of distinct characters is: %d\n", result);
    return 0;
}
```

This code will first initialize a vector to store the counts of each character, and then loop through the input string. For each character, it checks if the count of that character is 0 (which means it is a new character). If it is, it increments the count of distinct characters. Finally, it returns the count of distinct characters.

The time complexity of this solution is O(n), where n is the length of the string. This is because it needs to loop through the string once. The space complexity is also O(n), because the vector can grow up to the size of the string.

This code can be run in any C++ environment. Just copy and paste it into a new file and compile and run it.

This code works for ASCII characters only. If you want to support Unicode characters (like emoji), you would need a different approach that takes into account the encoding of these characters.

I hope this helps you understand the code better. If you have any other questions, feel free to ask.


















































































































