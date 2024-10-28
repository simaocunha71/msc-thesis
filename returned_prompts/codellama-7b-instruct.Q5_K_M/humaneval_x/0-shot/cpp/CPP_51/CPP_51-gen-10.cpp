    string::iterator i;
    for(i = text.begin(); i != text.end(); ++i){
        if(*i == 'a' || *i == 'e' || *i == 'i' || *i == 'o' || *i == 'u'){
            text.erase(i);
            goto A;
        }
    }
    return text;
}
int main(){
    string str;
    while(cin >> str){
        cout << remove_vowels(str) << endl;
    }
    return 0;
}
