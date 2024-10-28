    int largest_negative=0, smallest_positive=0;
    bool flag1=false, flag2=false;

    for(int i=0; i<lst.size(); i++){
        if(lst[i]<0 && lst[i]>largest_negative)
            largest_negative=lst[i];
        if(lst[i]>0 && (smallest_positive==0 || lst[i]<smallest_positive))
            smallest_positive=lst[i];
    }

    if(largest_negative==0)
        flag1=true;
    if(smallest_positive==0)
        flag2=true;

    return {flag1?0:largest_negative, flag2?0:smallest_positive};
}


A: I'm not sure what you're asking for, but I'll give you a couple of more examples.

