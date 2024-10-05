    if (arr.size()==0) return -32768;
    int sum=0, prod=1;
    for(int i=0; i<arr.size(); i++){
        sum += abs(arr[i]);
        prod*= (arr[i]>0)?1:-1;
    }
    return sum*prod;
}

