    int total=number+need;
    int left=remaining-need;
    if (left<0)
    total+=left;
    left=0;
    return vector<int>{total,left};
}


