    string res;
    int n=x;
    while(n>0)
    {
        int rem=n%base;
        if (rem<10)
            res=char(48+rem)+res;
        else
            res=char(55)+(char)(rem-10)+res;
        n=n/base;
    }
    return (n==0)?"0":res;
}
//48 is the ASCII value of '0', 55 is the ASCII value of 'A' - 10


