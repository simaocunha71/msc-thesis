    int i = word.length() - 1;
    while(i > 0){
        if("aeiouAEIOU".find(word[i]) != string::npos){
            if(i > 1 && !("aeiouAEIOU".find(word[i-1]) != string::npos) && !("aeiouAEIOU".find(word[i-2]) != string::npos)){
                return word.substr(i,1);
            }
        }
        i--;
    }
    return "";
}

int main(){
    printf("%s\n", get_closest_vowel("yogurt").c_str());
    printf("%s\n", get_closest_vowel("FULL").c_str());
    printf("%s\n", get_closest_vowel("quick").c_str());
    printf("%s\n", get_closest_vowel("ab").c_str());
    return 0;
}

