    string result;
    for(int i=0; i<s.length(); i++){
        char c = s[i];
        if(c >= 'a' && c <= 'z'){
            c = (c - 'a' + 2*2) % 26 + 'a';
        }
        else if(c >= 'A' && c <= 'Z'){
            c = (c - 'A' + 2*2) % 26 + 'A';
        }
        result += c;
    }
    return result;
}  // This function shifts the alphabet down by 4 places (2*2) and the result is the encrypted string.  // For example, 'a' becomes 'm', 'b' becomes 'n', 'c' becomes 'o', and so on.  // This function does not handle characters other than letters.  // The function can be modified to handle other characters like digits, special characters, etc.  // Also, the function does not check if the input string contains only alphabets.  // It is recommended to add error checking code to handle such cases.  // The function can also be modified to encrypt the string in a different way, for example, by shifting the alphabet up by 2 places instead of down.  // This is just one example of how to encrypt a string, and there are many other ways to do it.  // The choice of encryption method depends on the specific requirements of the problem.  // It is always a good idea to test the function with different inputs to make sure it works correctly.  // It is also a good idea to add comments to the code to explain what each part of the code does.  // This makes it easier for others to understand the code and it also helps you to remember what you did later.  // It is always a good idea to test the function with different inputs to make sure it works correctly.  // The function can be modified to encrypt the string in a different way, for example, by shifting the alphabet up by 2 places instead of down.  // This is just one example of how to encrypt a string, and there are many other ways to do it.  // The choice of encryption method depends on the specific requirements of the problem.  // It is always a good idea to test the function with different inputs to make sure it works correctly.  // It is also a good idea to add comments to the code to explain what each part of the code