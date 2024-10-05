    int i;
    int count=0;
    vector<char> distinct_chars;
    for (i=0;i<str.length();i++)
    {
        char chr=str[i];
        if (find(distinct_chars.begin(),distinct_chars.end(),chr)==distinct_chars.end())
        {
            distinct_chars.push_back(chr);
            count+=1;
        }
    }
    return count;
}


