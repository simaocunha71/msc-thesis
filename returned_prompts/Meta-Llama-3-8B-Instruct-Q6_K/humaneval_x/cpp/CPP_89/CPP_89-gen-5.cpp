    string encrypted = "";
    for(int i = 0; i < s.length(); i++){
        if(s[i] >= 'a' && s[i] <= 'z'){
            char c = s[i];
            c = (c - 'a' + 4 * 2) % 26 + 'a';
            encrypted += c;
        }
        else if(s[i] >= 'A' && s[i] <= 'Z'){
            char c = s[i];
            c = (c - 'A' + 4 * 2) % 26 + 'A';
            encrypted += c;
        }
        else{
            encrypted += s[i];
        }
    }
    return encrypted;
}

int main(){
    string s;
    cout<<"Enter a string to encrypt: ";
    cin>>s;
    cout<<"Encrypted string: "<<encrypt(s);
    return 0;
}

