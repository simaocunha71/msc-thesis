    int largest_negative =0;
    int smallest_positive =0;
    for(int num: lst){
        if(num<0 && num>largest_negative)
            largest_negative = num;
        if(num>0 && (smallest_positive==0 || num<smallest_positive))
            smallest_positive = num;
    }
    return {largest_negative, smallest_positive};
}


