    map<char,int> freq;
    for (int i=0;i<test.length();i++)
    {
        if (test[i]>='a' && test[i]<='z')
        {
            if (freq.count(test[i]))
            freq[test[i]]+=1;
            else
            freq[test[i]]=1;
        }
    }
    return freq;
}



