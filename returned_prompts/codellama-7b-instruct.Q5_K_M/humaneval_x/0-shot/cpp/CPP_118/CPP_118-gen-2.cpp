    int len = word.size();
    if(len < 2) return "";
    // find the first vowel
    for(int i = 0; i < len; i++){
        if(word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u'){
            int j = i + 1;
            while(j < len){
                if(word[j] != 'a' && word[j] != 'e' && word[j] != 'i' && word[j] != 'o' && word[j] != 'u'){
                    return word[i];
                }
                j++;
            }
        }
    }
    return "";
}
int main(){
    string word;
    getline(cin, word);
    printf("%s", get_closest_vowel(word).c_str());
}
