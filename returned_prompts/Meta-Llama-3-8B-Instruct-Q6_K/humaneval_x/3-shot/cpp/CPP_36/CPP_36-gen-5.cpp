    int count=0;
    for(int i=0;i<n;i++)
    {
        if(i%11==0 || i%13==0)
        {
            int num=i;
            while(num>0)
            {
                if(num%10==7)
                    count++;
                num=num/10;
            }
        }
    }
    return count;
}