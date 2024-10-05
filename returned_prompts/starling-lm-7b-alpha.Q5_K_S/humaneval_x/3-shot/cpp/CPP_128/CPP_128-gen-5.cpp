    int i;
    int total=0;
    int sign=1;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]==0){
            sign*=-1;
        }
        else{
        total+=abs(arr[i])*sign;
        sign*=-1;
        }
    }
    return total;
}



