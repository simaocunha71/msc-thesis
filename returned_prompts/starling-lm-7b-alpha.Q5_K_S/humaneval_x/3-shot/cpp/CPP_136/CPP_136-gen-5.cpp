    int i;
    int smallest=1000000001;
    int largest=-1000000001;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<smallest){
            smallest=lst[i];
        }
        if (lst[i]>largest){
            largest=lst[i];
        }
    }
    vector<int> result={largest,smallest};
    return result;
}




