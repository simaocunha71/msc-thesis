    if (n>m)
    {
        return "-1";
    }
    else
    {
        int average=(n+m)/2;
        string ans="";
        while (average>0)
        {
            ans+=char((average%2)+'0');
            average/=2;
        }
        return ans;
    }
}



