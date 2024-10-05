    vector<int> count(256,0);
    int i;
    for(i=0; i<str.length(); i++)
    count[tolower(str[i])]++;
    int total_distinct=0;
    for(i=0; i<256; i++)
    if(count[i]>0)
    total_distinct++;
    return total_distinct;
}


