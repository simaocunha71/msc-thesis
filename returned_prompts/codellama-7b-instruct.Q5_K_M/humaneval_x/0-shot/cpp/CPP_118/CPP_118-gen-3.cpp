    int i = 0;
    int len = word.length();
    for(i = 0; i < len; i++){
        if(word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u')
            break;
    }
    if(i == len)
        return "";
    else
        return word[i];
}
int main(){
    string word = "ab";
    string res = get_closest_vowel(word);
    printf("%s\n", res.c_str());
    return 0;
}
