    int count=0;
    int pos=0;
    while ((pos=str.find(substring)) != string::npos)
    {
        count++;
        pos++;
    }
    return count;
}