    long long min = INT_MAX;
    long long sum = 0;
    for(int i = 0; i < nums.size(); i++){
        sum += nums[i];
        min = min < sum ? min : sum;
        if(sum < 0) sum = 0;
    }
    return min;
}
int main(){