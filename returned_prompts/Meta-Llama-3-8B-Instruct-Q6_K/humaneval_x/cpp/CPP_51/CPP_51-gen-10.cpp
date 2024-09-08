    string new_str;
    for(int i = 0; i < text.length(); i++){
        if(text[i] != 'a' && text[i] != 'e' && text[i] != 'i' && text[i] != 'o' && text[i] != 'u' && text[i] != 'A' && text[i] != 'E' && text[i] != 'I' && text[i] != 'O' && text[i] != 'U'){
            new_str += text[i];
        }
    }
    return new_str;
}

int main(){
    string text;
    cout << "Enter the string: ";
    getline(cin, text);
    cout << remove_vowels(text);
    return 0;
}

