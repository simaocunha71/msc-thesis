    if(text[0]=='a'||text[0]=='A'||text[0]=='e'||text[0]=='E'||text[0]=='i'||text[0]=='I'||text[0]=='o'||text[0]=='O'||text[0]=='u'||text[0]=='U'){
        text.erase(text.begin());
        goto A;
    }
    return text;
}
int main() {
    string test;
    scanf("%s", &test);
    cout<<remove_vowels(test);
    return 0;
}
