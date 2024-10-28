    int i,j,sum=0;
    for (i=0;i<k;i++)
    for (j=0;j<100;j++)
    if (abs(arr[i]-j)<10){
        sum+=arr[i];
        break;
    }
    return sum;
}


