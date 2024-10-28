    if(arr.empty()){
        return -32768;
    }
    int prod_sign=1;
    int sum=0;
    for(int i=0;i<arr.size();i++){
        if(arr[i]<0){
            prod_sign*=-1;
        }
        else if(arr[i]>0){
            prod_sign*=1;
        }
        else{
            return 0;
        }
        sum+=abs(arr[i]);
    }
    return prod_sign*sum;
}



