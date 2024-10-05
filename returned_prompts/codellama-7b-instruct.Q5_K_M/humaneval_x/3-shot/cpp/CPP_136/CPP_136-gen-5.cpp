    int max_neg=-1;
    int min_pos=1;
    for (int i=0;i<lst.size();i++){
        if (lst[i]<0 && lst[i]>max_neg)
            max_neg=lst[i];
        if (lst[i]>0 && lst[i]<min_pos)
            min_pos=lst[i];
    }
    return vector<int>({max_neg, min_pos});
}


