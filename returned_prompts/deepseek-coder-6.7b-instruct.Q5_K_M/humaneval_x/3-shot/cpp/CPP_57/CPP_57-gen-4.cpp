    bool increasing=false;
    bool decreasing=false;
    for(int i=0;i<l.size()-1;i++)
    {
        if(l[i]<l[i+1])
        increasing=true;
        if(l[i]>l[i+1])
        decreasing=true;
    }
    return increasing && decreasing;
}


