    int n = s.length();
    string result = "";
    for(int i = 0; i < n; i++){
        char c = s[i];
        if(c >= 'a' && c <= 'z'){
            c = (c - 'a' + 2*2)%26 + 'a';
        }else if(c >= 'A' && c <= 'Z'){
            c = (c - 'A' + 2*2)%26 + 'A';
        }
        result += c;
    }
    return result;
}

int main(){
    string str;
    cout << "Enter a string: ";
    getline(cin, str);
    string encrypted = encrypt(str);
    cout << "Encrypted string: " << encrypted << endl;
    return 0;
}

