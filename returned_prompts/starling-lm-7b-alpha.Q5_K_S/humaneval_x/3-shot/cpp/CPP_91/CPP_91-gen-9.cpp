    int i,count=0;
    string word;
    for (i=0;i<S.length();i++)
    {
        char chr=S[i];
        if (chr=='.' || chr=='?' || chr=='!')
        {
        if (word=="I")
        count+=1;
        word="";
        }
        else
        word+=chr;
    }
    return count;
}


