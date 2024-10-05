    int sign_product=1;
    int sum_magnitudes=0;
    int i;
    if (arr.size()==0)
    return -32768;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]>0)
        sign_product*=1;
        if (arr[i]<0)
        sign_product*=-1;
        sum_magnitudes+=abs(arr[i]);
    }
    return sign_product*sum_magnitudes;
} 
*/



