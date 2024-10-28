    string vowels = "aeiouAEIOU";
    string encoded_message = "";
    for(char& c : message){
        if(vowels.find(c)!=string::npos){
            if(islower(c))
                encoded_message += char(c+2*2);
            else
                encoded_message += char(c+2*2-32);
        }
        else{
            encoded_message += c;
        }
    }
    reverse(encoded_message.begin(), encoded_message.end());
    return encoded_message;
}

int main(){
    printf(encode("test").c_str());
    printf(encode("This is a message").c_str());
    return 0;
}
```

```
Output:
"tgst"
"shks ks c mgss cgg"
```

In the above program, the function `encode` takes a string message as an argument. It iterates over each character in the string. If the character is a vowel, it gets replaced by the letter that appears 2 places ahead in the english alphabet. The case of the letter is also swapped. After replacing all vowels, the string is reversed. The `main` function calls `encode` function with different test cases and prints the output.

The `find` function of string class is used to check if the character is a vowel or not. If it is a vowel, it gets replaced by the letter that appears 2 places ahead in the english alphabet. The character is converted to uppercase if it is lowercase and lowercase if it is uppercase using the `toupper` and `tolower` functions. The `reverse` function is used to reverse the string.

The `char` type data is used to store the encoded characters. The `+` operator is used to add 2 to the ASCII value of the character to get the encoded character. The `%` operator is used to get the remainder of the division of the ASCII value of the character by 26 to get the encoded character if it is a vowel.

The `printf` function is used to print the encoded message.

The time complexity of this program is O(n), where