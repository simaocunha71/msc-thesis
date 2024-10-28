    string result;
    int i;
    for (i=0;i<=n;i++)
    {
        if (i!=0) result+=" ";
        char buffer[100];
        sprintf(buffer,"%d",i);
        result+=buffer;
    }
    return result;
}


