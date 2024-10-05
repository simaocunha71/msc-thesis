    int i;
    int max_neg=-1000;
    int min_pos=1000;
    int max_neg_index=-1;
    int min_pos_index=-1;
    for (i=0;i<lst.size();i++)
    if (lst[i]<0 && lst[i]>max_neg){
        max_neg=lst[i];
        max_neg_index=i;
    }
    for (i=0;i<lst.size();i++)
    if (lst[i]>0 && lst[i]<min_pos){
        min_pos=lst[i];
        min_pos_index=i;
    }
    return vector<int>{max_neg_index,min_pos_index};
}



