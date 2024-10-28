    int largest_negative =0;
    int smallest_positive =0;
    bool has_positive = false;
    bool has_negative = false;
    for (int i=0;i<lst.size();i++){
        if (lst[i]<0 && (has_negative == false || lst[i]>largest_negative)){
            largest_negative = lst[i];
            has_negative = true;
        }
        if (lst[i]>0 && (has_positive == false || lst[i]<smallest_positive)){
            smallest_positive = lst[i];
            has_positive = true;
        }
    }
    if (!has_negative){
        largest_negative = 0;
    }
    if (!has_positive){
        smallest_positive = 0;
    }
    return {largest_negative,smallest_positive};
}

