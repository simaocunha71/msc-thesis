    int n = arr.size();
    if(n==0) return {};
    vector<int> res;
    int min_val = INT_MAX;
    int min_idx = -1;
    for(int i=0;i<n;i++){
        if(arr[i] < min_val && arr[i]%2 == 0){
            min_val = arr[i];
            min_idx = i;
        }
    }
    if(min_idx == -1) return {};
    res.push_back(min_val);
    res.push_back(min_idx);
    return res;
}

int main()
{
    vector<int> res, arr = {5, 0, 3, 0, 4, 2};
    res = pluck(arr);
    for(int i=0; i<res.size(); i++)
    {
       printf("%d ", res[i]);
    }
    return 0;
}
/*
Output: 0 1
*/

