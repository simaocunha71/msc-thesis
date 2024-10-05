    long long sum=0,min_sum=0;
    for(auto num:nums){
        sum+=num;
        if(sum<min_sum)
            min_sum=sum;
    }
    return -min_sum+1;
}


