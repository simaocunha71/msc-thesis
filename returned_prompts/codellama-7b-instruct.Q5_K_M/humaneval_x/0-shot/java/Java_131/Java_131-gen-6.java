        while(n!=0)
        {
            if(n%10%2==1)
            {
                return n*n;
            }
            n/=10;
        }
        return 0;
    }
}



