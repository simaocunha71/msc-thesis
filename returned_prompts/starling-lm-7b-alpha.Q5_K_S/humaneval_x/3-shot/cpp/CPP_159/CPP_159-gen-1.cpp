    int total=number+need;
    int left=remaining-need;
    if (left>0)
    {
        total+=left;
        left=0;
    }
    return {total,left};
}



