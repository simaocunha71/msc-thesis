    int count=0;
    int str_len=str.length();
    int sub_len=substring.length();
    for (int i=0;i<=str_len-sub_len;i++)
    {
        if (str.substr(i,sub_len)==substring)
        count++;
    }
    return count;
}