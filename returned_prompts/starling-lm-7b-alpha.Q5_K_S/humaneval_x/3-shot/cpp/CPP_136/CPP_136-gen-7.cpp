    int i;
    int neg_max=-10000000;
    int pos_min=10000000;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<0 && lst[i]>neg_max){
        neg_max=lst[i];
        }
        if (lst[i]>0 && lst[i]<pos_min){
        pos_min=lst[i];
        }
    }
    vector<int> result={neg_max,pos_min};
    return result;
}


