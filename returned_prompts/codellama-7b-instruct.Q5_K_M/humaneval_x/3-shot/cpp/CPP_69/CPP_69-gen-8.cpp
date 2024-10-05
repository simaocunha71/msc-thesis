    int i,j;
    int max_val;
    int max_freq;
    int freq;
    int curr_val;

    max_val=0;
    max_freq=0;
    freq=0;

    for (i=0;i<lst.size();i++){
        curr_val=lst[i];
        for (j=0;j<lst.size();j++)
        if (curr_val==lst[j])
        freq+=1;
        if (max_val<curr_val && freq>=curr_val){
            max_val=curr_val;
            max_freq=freq;
        }
    }
    if (max_freq>=max_val)
    return max_val;
    else
    return -1;
}




