    string result;
    for(int i = 0; i < s.length(); i++){
        char ch = s[i];
        if(ch >= 'a' && ch <= 'z'){
            int shift = 2 * 2;
            ch = (ch - 'a' + shift) % 26 + 'a';
        }
        else if(ch >= 'A' && ch <= 'Z'){
            int shift = 2 * 2;
            ch = (ch - 'A' + shift) % 26 + 'A';
        }
        result += ch;
    }
    return result;
}

int main()
{
    string s;
    printf("Enter a string to encrypt: ");
    cin >> s;
    cout << "Encrypted string: " << encrypt(s) << endl;
    return 0;
}

