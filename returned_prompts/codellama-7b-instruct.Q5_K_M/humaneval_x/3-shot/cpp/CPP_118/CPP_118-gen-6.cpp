    string closest_vowel="";
    char ch;
    int i;
    for (i=word.length()-1;i>=0;i--){
        ch=word[i];
        if (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'){
            closest_vowel=ch;
            break;
        }
    }
    return closest_vowel;
}


