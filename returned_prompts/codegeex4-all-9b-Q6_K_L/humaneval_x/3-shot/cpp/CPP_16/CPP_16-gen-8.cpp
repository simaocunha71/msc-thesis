    int count=0;
    vector<char> char_vec;
    char chr;
    int i;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        transform(chr,chr+1,chr,tolower);
        if (find(char_vec.begin(),char_vec.end(),chr)==char_vec.end())
        {
        char_vec.push_back(chr);
        count+=1;
        }
    }
    return count;
}

