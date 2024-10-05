    int count = 0;
    int sum = 0;
    for(int i = 0; i < n.size(); i++){
        int num = n[i];
        while(num){
            sum += num % 10;
            num /= 10;
        }
        if(sum > 0){
            count++;
        }
        sum = 0;
    }
    return count;
}

int main(){
    vector<int> nums = {1, 1, 2};
    printf("%d\n", count_nums(nums));
    return 0;
}
```

