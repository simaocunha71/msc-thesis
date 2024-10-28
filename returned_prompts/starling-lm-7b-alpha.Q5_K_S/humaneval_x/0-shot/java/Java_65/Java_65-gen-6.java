    for(int i=shift;i<shift+x;i++)
    {
        int y=x;
        while(y!=0)
        {
            int temp=y%10;
            y/=10;
        }
        if(i>shift+x-1)
        {
            while(i>shift+x-1)
            {
                int temp=x%10;
                x/=10;
                i++;
                if(temp!=0)
                {
                    System.out.print(temp);
                }
                else
                {
                    continue A;
                }
            }
        }
        else
        {
            while(i!=shift+x-1)
            {
                int temp=x%10;
                x/=10;
                i++;
                if(temp!=0)
                {
                    System.out.print(temp);
                }
                else
                {
                    continue A;
                }
            }
        }
    }
    }
}
















































































































































































































































