    string s="";
    int n=x;
    int i;
    while (n>0)
    {
        s+=n%10;
        n=n/10;
    }
    if (shift>s.length())
    {
        reverse(s.begin(),s.end());
        return s;
    }
    else
    {
        int l=s.length();
        shift=shift%l;
        s=s.substr(l-shift,l);
        s=s+s.substr(0,l-shift);
        return s;
    }
}

