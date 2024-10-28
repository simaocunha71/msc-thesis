    int count=0;
    int len=num.length();
    for (int i=0;i<len;i++)
    if (is_hex(num[i]))
    count+=hex_key(num.substr(i,1));
    return count;
}



