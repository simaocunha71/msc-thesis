    int n=nums.size();
    long long min=0;
    for(int i=0;i<n;i++){
        long long sum=0;
        for(int j=i;j<n;j++){
            sum+=nums[j];
            if(sum<min){
                min=sum;
            }
        }
    }
    return min;
}

