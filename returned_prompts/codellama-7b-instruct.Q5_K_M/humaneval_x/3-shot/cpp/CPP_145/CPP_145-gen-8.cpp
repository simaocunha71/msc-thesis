    vector<pair<int,int>> num_index;
    vector<int> ordered_nums;
    int i;
    for (i=0;i<nums.size();i++)
    num_index.push_back({sum_digits(nums[i]),i});

    sort(num_index.begin(), num_index.end());
    for (auto p:num_index)
    ordered_nums.push_back(nums[p.second]);
    return ordered_nums;
}

int sum_digits(int n){
int sum=0;
while (n)
sum+=n%10, n/=10;
return sum;
}


