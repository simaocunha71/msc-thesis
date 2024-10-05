    string max="";
    int max_count=0;
    int count=0;
    string current;

    for (int i=0;i<words.size();i++)
    {
        current=words[i];
        sort(current.begin(),current.end());

        count=0;
        char chr;
        for (int j=0;j<current.length();j++)
        {
            chr=current[j];
            if (chr!=current[j+1])
            count+=1;
        }

        if (count>max_count)
        {
            max_count=count;
            max=current;
        }
    }

    return max;
}

