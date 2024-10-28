    int i;
    int count=0;
    string temp;
    for(i=1;i<n;i++)
    {
        if(i%11==0||i%13==0)
        {
            temp=to_string(i);
            for(char c : temp)
            {
                if(c=='7')
                {
                    count+=1;
                }
            }
        }
    }
    return count;
}


