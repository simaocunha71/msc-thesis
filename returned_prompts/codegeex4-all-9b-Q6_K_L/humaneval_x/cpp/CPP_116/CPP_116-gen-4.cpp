    sort(arr.begin(),arr.end());
    for(int i=0;i<arr.size();i++){
        int count=0;
        int x=arr[i];
        while(x!=0){
            if(x%2==1){
                count++;
            }
            x=x/2;
        }
        arr[i]=count*10000+arr[i];
    }
    sort(arr.begin(),arr.end());
    return arr;
}
