    int count=0;
    for(int i=0;i<num.length();i++)
    {
        if((num[i]>='2'&&num[i]<='9')||(num[i]>='A'&&num[i]<='F'))
        {
            if(num[i]=='2'||num[i]=='3'||num[i]=='5'||num[i]=='7'||num[i]=='B'||num[i]=='D')
            {
                count++;
            }
        }
    }
    return count;
}