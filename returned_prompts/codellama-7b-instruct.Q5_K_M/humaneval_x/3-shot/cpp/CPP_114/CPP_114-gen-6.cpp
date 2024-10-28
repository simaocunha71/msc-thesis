    int i,j;
    int current_sum=0;
    int min_sum=0;
    int size=nums.size();
    for (i=0;i<size;i++){
        current_sum+=nums[i];
        min_sum=min(current_sum, min_sum);
        if (current_sum<0){
            current_sum=0;
        }
    }
    return min_sum;
}



