    int i,j;
    int largest_neg,smallest_pos;
    largest_neg=INT_MIN;
    smallest_pos=INT_MAX;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<0 && lst[i]>largest_neg){
            largest_neg=lst[i];
        }
        if (lst[i]>0 && lst[i]<smallest_pos){
            smallest_pos=lst[i];
        }
    }
    vector<int> ret;
    ret.push_back(largest_neg);
    ret.push_back(smallest_pos);
    return ret;
}


