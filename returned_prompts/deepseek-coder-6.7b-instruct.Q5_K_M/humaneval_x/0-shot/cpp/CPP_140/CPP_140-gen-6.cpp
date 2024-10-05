string res="";

for(int i=0; i<text.size(); i++){
    if(text[i] == ' '){
        if(i+1<text.size() && text[i+1] == ' '){
            res+='-';
            while(i<text.size() && text[i] == ' ')
                i++;
        }
        else{
            res+='_';
        }
    }
    else{
        res+=text[i];
    }
}
return res;
}

int main() {
    printf("%s\n", fix_spaces("Example").c_str());
    printf("%s\n", fix_spaces("Example 1").c_str());
    printf("%s\n", fix_spaces(" Example 2").c_str());
    printf("%s\n", fix_spaces(" Example  3").c_str());
    return 0;
}
```

**Explanation**

This program takes in a string as input and returns the string with all spaces replaced by underscores. If the string contains more than two consecutive spaces, it replaces these spaces with a dash.

The solution uses a for loop to iterate over each character in the input string. If a character is a space, the program checks the next character. If it's also a space, the program appends a dash to the result string and skips the rest of the consecutive spaces in the input string. If the next character is not a space, the program appends an underscore to the result string. If a character is not a space, it's appended to the result string as is.

The function returns the result string.

In the main function, we use the function to test it with different strings.

**Time Complexity**

The time complexity of this program is O(n), where n is the length of the input string. This is because the program makes a single pass over the input string.

**Space Complexity**

The space complexity of this program is also O(n), where n is the length of the input string. This is because the program creates a new string that is at most one character longer than the input string.
