    int i;
    for(i=2;i<100;i++)
    {
        if(a%i==0)
        {
            int j;
            for(j=2;j<100;j++)
            {
                if((i%j==0)&&(a%j==0))
                {
                    return false;
                }
            }
        }
    }
    return true;
}


