    string new_sentence;
    int space=0;
    int i;
    int j;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]==' ')
        {
            space+=1;
            continue;
        }
        for (j=i+1;j<sentence.length();j++)
        {
            if (sentence[j]==' ')
            {
                new_sentence+=sentence.substr(i, j-i);
                i=j;
                break;
            }
        }
    }
    return new_sentence;
}


