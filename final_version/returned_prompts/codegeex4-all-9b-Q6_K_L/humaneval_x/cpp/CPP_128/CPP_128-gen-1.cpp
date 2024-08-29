    int prod=1;
    int sum=0;
    int sign;
    int i;

    if(arr.size()==0){
        return -32768;
    }
    for(i=0;i<arr.size();i++){
        sign=1;
        while(arr[i]<0){
            sign=-1;
            arr[i]=arr[i]*sign;
        }
        while(arr[i]==0){
            return 0;
        }
        sum+=arr[i];
        prod*=sign;
    }
    return prod*sum;
}
