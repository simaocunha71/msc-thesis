    if (lst.size()<2)
    return NULL;

    int first_min=INT_MAX, second_min=INT_MAX;
    for(int i=0;i<lst.size();i++){
        if(lst[i]<first_min)
            first_min=lst[i];
    }
    for(int i=0;i<lst.size();i++){
        if(lst[i]<second_min && lst[i]>first_min)
            second_min=lst[i];
    }
    if (second_min==INT_MAX)
        return NULL;
    else 
        return second_min;
}


