    int i;
    for(i=word.length()-1;i>=0;i--){
        if((word[i]=='a' || word[i]=='e' || word[i]=='i' || word[i]=='o' || word[i]=='u') && i>0 && !isalpha(word[i-1]) && !isalpha(word[i+1])){
            return word.substr(i,1);
        }
    }
    return "";
} // end function get_closest_vowel


