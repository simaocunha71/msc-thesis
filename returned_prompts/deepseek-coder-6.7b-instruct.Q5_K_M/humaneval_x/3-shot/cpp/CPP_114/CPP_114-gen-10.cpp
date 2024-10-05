    long long sum = 0;
    long long min_sum = 0;
    for(auto n : nums){
        sum += n;
        if(sum < min_sum)
            min_sum = sum;
    }
    return min_sum;
}


