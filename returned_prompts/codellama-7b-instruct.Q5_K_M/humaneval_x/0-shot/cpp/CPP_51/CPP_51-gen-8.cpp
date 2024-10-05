    if(text.empty()) return "";
    for(int i=0;i<text.size();i++){
        if(text[i]=='a'||text[i]=='A'||text[i]=='e'||text[i]=='E'||text[i]=='i'||text[i]=='I'||text[i]=='o'||text[i]=='O'||text[i]=='u'||text[i]=='U'){
            text.erase(text.begin()+i);
            i--;
        }
    }
    goto A;
}

int main() {
    string text;
    printf("Please input a string:\n");
    getline(cin, text);
    string result = remove_vowels(text);
    printf("The result is:\n");
    cout<<result;
    return 0;
}
