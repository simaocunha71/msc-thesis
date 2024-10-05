    string vowels="aeiou";
    string result="";
    int i;
    bool is_vowel;
    for (i=0;i<word.length();i++)
    {
        is_vowel=false;
        for (char chr:vowels)
        if (word[i]==chr)
        {
            is_vowel=true;
            break;
        }

        if (i>0 && i<word.length()-1 && is_vowel && word[i-1]!='a' && word[i+1]!='a' &&
            word[i]!=word[i-1] && word[i]!=word[i+1])
        {
            result=word[i];
            break;
        }
    }
    return result;
}


