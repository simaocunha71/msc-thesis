    vector<int> arr(n+1,0);
    arr[0]=1;
    arr[1]=3;
    arr[2]=2;
    for(int i=3;i<=n;i++){
        if(i%2==0){
            arr[i]=arr[i-1]+arr[i-2];
        }else{
            arr[i]=arr[i-1]+arr[i-2]+arr[i+1];
        }
    }
    return arr;
}
