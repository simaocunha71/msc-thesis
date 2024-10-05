    if (n>m) return "-1";
    int i,avg=(n+m)/2;
    string binary_str;
    for (i=15;i>=0;i--)
    {
        binary_str+=((1<<i)&avg)?'1':'0';
    }
    return binary_str;
}


