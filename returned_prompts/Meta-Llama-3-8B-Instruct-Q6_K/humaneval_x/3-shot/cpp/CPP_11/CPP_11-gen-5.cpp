    string result;
    int i,a_len,b_len;
    a_len=a.length();
    b_len=b.length();
    for (i=0;i<max(a_len,b_len);i++)
    {
        int bit_a=0,bit_b=0;
        if (i<a_len) bit_a=(a[i]-'0');
        if (i<b_len) bit_b=(b[i]-'0');
        result+=char((bit_a^bit_b)+'0');
    }
    return result;
}