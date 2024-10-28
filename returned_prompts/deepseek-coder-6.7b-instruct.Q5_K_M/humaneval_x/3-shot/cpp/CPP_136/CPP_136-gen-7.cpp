    int largest_negative=0, smallest_positive=0, found=0;
    for(int i=0; i<lst.size(); i++){
        if(lst[i]<0 && lst[i]>largest_negative)
            largest_negative=lst[i];
        if(lst[i]>0 && (smallest_positive==0 || lst[i]<smallest_positive))
            smallest_positive=lst[i];
    }
    if(largest_negative==0)
        found++;
    if(smallest_positive==0)
        found++;
    if(found==2)
        return {0,0};
    return {largest_negative, smallest_positive};
}

