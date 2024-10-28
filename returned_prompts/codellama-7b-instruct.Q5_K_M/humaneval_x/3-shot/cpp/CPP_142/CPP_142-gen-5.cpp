    int i;
    int sum;
    int index;
    int square;
    for (i=0;i<lst.size();i++){
        index=i+1;
        square=lst[i]*lst[i];
        if (index%3==0 && index%4!=0)
        sum+=square;
        if (index%4==0 && index%3!=0)
        sum+=lst[i]*lst[i]*lst[i];
    }
    return sum;
}


