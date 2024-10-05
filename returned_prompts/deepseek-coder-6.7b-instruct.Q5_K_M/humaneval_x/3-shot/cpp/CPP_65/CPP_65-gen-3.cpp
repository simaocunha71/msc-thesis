    string str = to_string(x);
    int len = str.length();
    if(shift>=len)
    {
        reverse(str.begin(), str.end());
        return str;
    }
    else
    {
        rotate(str.begin(),str.begin()+str.length()-shift,str.end());
        return str;
    }
}

