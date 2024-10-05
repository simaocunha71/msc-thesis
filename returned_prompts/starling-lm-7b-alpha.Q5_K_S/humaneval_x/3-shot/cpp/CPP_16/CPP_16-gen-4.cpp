    vector<char> chars;
    char chr;
    for (char chr: str)
    chars.push_back(tolower(chr));
    sort(chars.begin(),chars.end());
    int i;
    int size=chars.size();
    int count=0;
    for (i=0;i<size;i++)
    if (i==size-1 || chars[i]!=chars[i+1])
    count+=1;
    return count;
}


