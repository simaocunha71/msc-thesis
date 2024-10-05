    int i,j;
    for (i=2;i<10;i++)
    {
        if (a%i==0)
        {
            for (j=2;j<10;j++)
            {
                if (i%j==0)
                return false;
            }
            break;
        }
    }
    return true;
}


