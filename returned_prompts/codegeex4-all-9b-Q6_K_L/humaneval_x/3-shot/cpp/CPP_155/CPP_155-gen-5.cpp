    int count[2]={0};
    string str_num=to_string(num);
    int i;
    for (i=0;i<str_num.length();i++)
    {
        if (str_num[i]%2==0)
            count[0]+=1;
        else
            count[1]+=1;
    }
    return count;
}

