    int largest_neg=0, smallest_pos=0;
    bool flag_neg=false, flag_pos=false;
    for(int i=0;i<lst.size();i++){
        if(lst[i]<0 && lst[i]>largest_neg){
            largest_neg=lst[i];
            flag_neg=true;
        }
        if(lst[i]>0 && (smallest_pos==0 || lst[i]<smallest_pos)){
            smallest_pos=lst[i];
            flag_pos=true;
        }
    }
    if(!flag_neg) largest_neg=0;
    if(!flag_pos) smallest_pos=0;
    return {largest_neg,smallest_pos};
}


