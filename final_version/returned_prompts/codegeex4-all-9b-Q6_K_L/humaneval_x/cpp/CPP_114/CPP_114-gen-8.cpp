    int n = nums.size();
    long long ans = 1000000000000000000;
    for(int i = 0; i < n; i++)
    {
        long long sum = 0;
        for(int j = i; j < n; j++)
        {
            sum += nums[j];
            if(sum < ans) ans = sum;
        }
    }
    return ans;
}

B:
    long long ans = nums[0];
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] < ans) ans = nums[i];
    }
    return ans;

C:
    int n = nums.size();
    long long ans = 1000000000000000000;
    for(int i = 0; i < n; i++)
    {
        long long sum = 0;
        for(int j = i; j < n; j++)
        {
            sum += nums[j];
            if(sum < ans) ans = sum;
        }
    }
    return ans;

D:
    int n = nums.size();
    long long ans = 1000000000000000000;
    for(int i = 0; i < n; i++)
    {
        long long sum = 0;
        for(int j = i; j < n; j++)
        {
            sum += nums[j];
            if(sum < ans) ans = sum;
        }
    }
    return ans;

E:
    int n = nums.size();
    long long ans = 1000000000000000000;
    for(int i = 0; i < n; i++)
    {
        long long sum = 0;
        for(int j = i; j < n; j++)
        {
            sum += nums[j];
            if(sum < ans) ans = sum;
        }
    }
    return ans;

F:
    int n = nums.size();
    long long ans = 1000000000000000000;
    for(int i = 0; i < n; i++)
    {
        long long sum = 0;
        for(int j = i; j < n; j++)
        {
            sum += nums[j];
            if(sum < ans) ans = sum;
        }
    }
    return ans;

G:
    int n = nums.size();
    long long ans = 1000000000000000000;
    for(int i = 0; i < n; i++)
   