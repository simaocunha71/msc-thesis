    if(arr.empty()) return -32768;
    int sign = 1;
    long long sum=0;
    for(int i=0; i<arr.size(); i++){
        if(arr[i]!=0){
            sign *= (arr[i]>=0 ? 1 : -1);
            sum += abs(arr[i]);
        }
    }
    return sign*sum;
}

