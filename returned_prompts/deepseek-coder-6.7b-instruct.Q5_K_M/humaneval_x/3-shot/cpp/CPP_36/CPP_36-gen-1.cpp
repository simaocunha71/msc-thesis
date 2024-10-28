    int i,count=0;
    char buffer[50];
    for(i=1;i<n;i++)
    if((i%11==0 || i%13==0) && sprintf(buffer,"%d",i) && strchr(buffer,'7'))
        count++;
    return count;
}



