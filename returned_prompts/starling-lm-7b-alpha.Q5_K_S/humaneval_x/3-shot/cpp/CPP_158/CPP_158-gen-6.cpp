    string res="";
    int max_count=0;
    int i;
    for (i=0;i<words.size();i++)
    {
        string word=words[i];
        int count=0;
        for (int j=0;j<word.size();j++)
        {
            bool found=false;
            for (int k=0;k<res.size();k++)
            {
                if (res[k]==word[j])
                {
                    found=true;
                    break;
                }
            }
            if (!found)
            {
                count+=1;
            }
        }
        if (count>max_count)
        {
            max_count=count;
            res=word;
        }
    }
    return res;
}


