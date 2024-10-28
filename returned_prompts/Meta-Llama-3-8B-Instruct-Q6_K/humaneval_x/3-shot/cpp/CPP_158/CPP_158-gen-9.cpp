    string max_word;
    int max_length=0;
    for (int i=0;i<words.size();i++)
    {
        int count=0;
        for (int j=0;j<words[i].length();j++)
        {
            bool found=false;
            for (int k=0;k<count;k++)
            {
                if (words[i][j]==max_word[k])
                {
                    found=true;
                    break;
                }
            }
            if (!found)
            {
                count++;
                max_word+=words[i][j];
            }
        }
        if (count>max_length)
        {
            max_length=count;
            max_word=words[i];
        }
    }
    return max_word;
} // end of function find_max


