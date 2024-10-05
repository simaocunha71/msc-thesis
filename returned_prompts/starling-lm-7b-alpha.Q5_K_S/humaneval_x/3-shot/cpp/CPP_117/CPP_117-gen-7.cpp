    vector<string> all_words;
    vector<string> current_word;
    char chr;
    int consonants=0;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (isalpha(chr))
        {
            if (consonants==n)
            {
                if (current_word.size()>0)
                {
                all_words.push_back(current_word);
                current_word="";
                }
            }
            else if (consonants<n)
            {
                if (isvowel(chr))
                {
                current_word.push_back(chr);
                consonants+=1;
                }
                else
                {
                    consonants+=1;
                }
            }
        }
    }
    return all_words;
}

bool isvowel(char chr){
    char c='a';
    return chr==c||chr=='e'||chr=='i'||chr=='o'||chr=='u';
}




