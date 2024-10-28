    int i;
    string vowel="";
    bool find_vowel=false;
    for (i=word.length()-1;i>0;i--)
    {
        if (word[i]=='a' || word[i]=='e' || word[i]=='o' || word[i]=='u' || word[i]=='i' || word[i]=='y')
        {
            if (word[i+1]=='a' || word[i+1]=='e' || word[i+1]=='o' || word[i+1]=='u' || word[i+1]=='i' || word[i+1]=='y')
            {
            if (find_vowel==false)
            {
                vowel=word[i];
                find_vowel=true;
            }
            }
        }
    }
    return vowel;
}


