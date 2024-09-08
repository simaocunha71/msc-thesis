    // Remove all non-alphanumeric characters from the string
    string cleaned_text = "";
    for(int i = 0; i < text.length(); i++){
        if(isalnum(text[i])){
            cleaned_text += tolower(text[i]);
        }
    }
    // Compare the cleaned string with its reverse
    string reversed_text = cleaned_text;
    reverse(reversed_text.begin(), reversed_text.end());
    if(cleaned_text == reversed_text){
        return true;
    }else{
        return false;
    }
}
int main(){
    cout << boolalpha;
    cout << is_palindrome("") << endl;
    cout << is_palindrome("aba") << endl;
    cout << is_palindrome("aaaaa") << endl;
    cout << is_palindrome("zbcd") << endl;
    return 0;
}

