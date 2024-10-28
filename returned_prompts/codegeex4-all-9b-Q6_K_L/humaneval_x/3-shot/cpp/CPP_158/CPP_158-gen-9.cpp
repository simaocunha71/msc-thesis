    int max=0;
    string current_max="";
    int i,j;
    char chr;
    for (i=0;i<words.size();i++)
    {
        string word=words[i];
        int unique=0;
        for (j=0;j<word.length();j++)
        {
            chr=word[j];
            if (count(word.begin(),word.end(),chr)==1)
            unique+=1;
        }
        if (unique>max)
        {
            current_max=word;
            max=unique;
        }
        else if (unique==max)
        {
            if (word<current_max)
            {
                current_max=word;
                max=unique;
            }
        }
    }
    return current_max;
}

