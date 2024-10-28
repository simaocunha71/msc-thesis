    int i;
    bool flag;
    string chr;
    for (auto i:dict)
    {
        chr=i.first;
        flag=false;
        for (int j=0;j<chr.length();j++)
        if (chr[j]>=97 && chr[j]<=122)
            flag=true;
        if (flag==true)
        {
            for (int j=0;j<chr.length();j++)
                if (chr[j]>=65 && chr[j]<=90)
                    return false;
        }
        else
        {
            for (int j=0;j<chr.length();j++)
                if (chr[j]>=97 && chr[j]<=122)
                    return false;
        }
    }
    return true;
}

