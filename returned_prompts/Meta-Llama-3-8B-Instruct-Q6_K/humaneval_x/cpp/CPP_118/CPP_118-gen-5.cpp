    string closest_vowel="";
    int i=word.length()-1;
    while(i>=0&&!(word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u')){
        i--;
    }
    if(i<0){
        return closest_vowel;
    }
    if(i==word.length()-1){
        return closest_vowel;
    }
    while(i>=0&&!(word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u')){
        i--;
    }
    closest_vowel=word.substr(i+1);
    return closest_vowel;
}
int main(){
    string word="yogurt";
    cout<<get_closest_vowel(word)<<endl;
    return 0;
}

