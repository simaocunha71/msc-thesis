    int i,j,k;
    int prime[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
    for (i=0;i<20;i++)
    if (a%prime[i]==0)
        return true;

    return false;
}



