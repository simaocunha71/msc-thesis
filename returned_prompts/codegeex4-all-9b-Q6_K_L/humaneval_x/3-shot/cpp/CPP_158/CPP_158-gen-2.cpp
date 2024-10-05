    int max=0;
    int i,j;
    string max_word="";
    for (i=0;i<words.size();i++)
    {
        string word=words[i];
        int unique_chars=0;
        for (j=0;j<word.length();j++)
        {
            char chr=word[j];
            if (word.find(chr,0)==j)
                unique_chars+=1;
        }
        if (unique_chars>max)
        {
            max=unique_chars;
            max_word=word;
        }
        if (unique_chars==max)
        {
            if (word<max_word)
                max_word=word;
        }
    }
    return max_word;
}

