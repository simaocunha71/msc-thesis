        int c=a%10;
        int d=b%10;
        int m=a/10;
        int n=b/10;
        if(c==0 && d==0)
        {
            return 0;
        }
        else
        {
            while(c!=0 && d!=0)
            {
                if(c>d)
                {
                    c=c%d;
                }
                else
                {
                    d=d%c;
                }
            }
            if(c==0 && d!=0)
            {
                while(d!=0)
                {
                    d=d%c;
                }
            }
            if(c!=0 && d==0)
            {
                while(c!=0)
                {
                    c=c%d;
                }
            }
            if(c==0 && d==0)
            {
                while(m!=0 && n!=0)
                {
                    if(m>n)
                    {
                        m=m%n;
                    }
                    else
                    {
                        n=n%m;
                    }
                }
                if(m==0 && n!=0)
                {
                    while(n!=0)
                    {
                        n=n%m;
                    }
                }
                if(m!=0 && n==0)
                {
                    while(m!=0)
                    {
                        m=m%n;
                    }
                }
                if(m==0 && n==0)
                {
                    break;
                }
            }
        }
        return c*d;
    }
}




































































