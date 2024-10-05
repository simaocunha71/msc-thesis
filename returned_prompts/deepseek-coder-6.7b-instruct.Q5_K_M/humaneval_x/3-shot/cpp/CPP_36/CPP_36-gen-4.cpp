    int count=0;
    string temp;
    for(int i=0;i<n;i++)
    {
        if(i%11==0||i%13==0)
        {
            temp=to_string(i);
            for(int j=0;j<temp.size();j++)
            {
                if(temp[j]=='7')
                {
                    count++;
                }
            }
        }
    }
    return count;
}

