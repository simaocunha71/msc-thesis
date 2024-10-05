    int largestNegative = 0;
    int smallestPositive = 0;
    bool flag1 = false, flag2 = false;

    for(int i = 0; i < lst.size(); i++){
        if(lst[i] < 0 && lst[i] > largestNegative){
            largestNegative = lst[i];
            flag1 = true;
        }
        else if(lst[i] > 0 && (smallestPositive == 0 || lst[i] < smallestPositive)){
            smallestPositive = lst[i];
            flag2 = true;
        }
    }

    if(!flag1)
        largestNegative = 0;
    if(!flag2)
        smallestPositive = 0;

    return {largestNegative, smallestPositive};
}


