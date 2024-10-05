    int count=0;
    for(int i=0;i<n;i++)
    {
        if(i%11==0||i%13==0)
        {
            string s=to_string(i);
            for(int j=0;j<s.length();j++)
            {
                if(s[j]=='7')
                {
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}

