    int sum, total=0;
    for(int i=0;i<n.size();i++)
    {
        if(n[i]<0)
        {
            sum=0;
            for(char c:to_string(-n[i]))
            sum+=c-'0';
            if(-sum>0) total++;
        }
        else
        {
            sum=0;
            for(char c:to_string(n[i]))
            sum+=c-'0';
            if(sum>0) total++;
        }
    }
    return total;
}


