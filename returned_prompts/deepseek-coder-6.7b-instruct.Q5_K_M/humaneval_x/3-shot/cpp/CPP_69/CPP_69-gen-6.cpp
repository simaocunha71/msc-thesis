    int freq[10] = {0};
    int i;
    for(i = 0; i < lst.size(); i++)
        freq[lst[i]]++;
    for(i = 10; i > 0; i--)
        if(freq[i] >= i)
            return i;
    return -1;
}

