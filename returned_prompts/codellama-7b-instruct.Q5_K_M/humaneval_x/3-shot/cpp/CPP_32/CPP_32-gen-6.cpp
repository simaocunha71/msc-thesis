    if (xs.size()%2==0&&xs[xs.size()-1]!=0)
    {
        return -xs[xs.size()-2]/xs[xs.size()-3];
    }
    else
    {
        printf("No zero found");
        return 0;
    }
}


