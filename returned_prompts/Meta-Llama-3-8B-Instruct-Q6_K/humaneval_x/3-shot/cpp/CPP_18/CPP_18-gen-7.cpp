    int count=0;
    int pos=str.find(substring);
    while (pos!=string::npos)
    {
        count++;
        pos=str.find(substring,pos+1);
    }
    return count;
} 

