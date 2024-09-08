    int n = s.size();
    string result = "";
    for(int i=0; i<n; i++){
        char c = s[i];
        if(c >= 'a' && c <= 'z'){
            c = (c - 'a' + 4*2) % 26 + 'a';
        }
        else if(c >= 'A' && c <= 'Z'){
            c = (c - 'A' + 4*2) % 26 + 'A';
        }
        result += c;
    }
    return result;
}
int main(){
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    cout << "Encrypted string: " << encrypt(s) << endl;
    return 0;
}

S:
The code defines a function `encrypt` that takes a string `s` as an argument and returns an encrypted string. The function iterates over each character `c` in the input string. If the character is a lowercase letter, it is shifted down by 8 places (4*2) in the alphabet. If the character is an uppercase letter, it is also shifted down by 8 places. The resulting character is then added to the result string. The function returns the encrypted string.

The `main` function prompts the user to enter a string, encrypts the string using the `encrypt` function, and prints the encrypted string to the console.

Note: The code assumes that the input string only contains letters (both lowercase and uppercase) and does not contain any other characters. If the input string contains other characters, the code may not work correctly.