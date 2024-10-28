    int i;
    int odd=0;
    int even=0;
    string str_num=to_string(abs(num));
    for (i=0;i<str_num.length();i++)
    {
        if ((str_num[i]-'0')%2==0)
        even+=1;
        else
        odd+=1;
    }
    return {odd,even};
}

