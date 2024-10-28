    vector<int> res;
    sort(arr.begin(), arr.end(), greater<int>());
    for(int i=0; i<k; i++){
        res.push_back(arr[i]);
    }
    sort(res.begin(), res.end());
    return res;
}

int main()
{
    vector<int> arr = {4, -4, 4};
    int k = 2;
    vector<int> res;
    res = maximum(arr,k);
    for(int i=0;i<res.size();i++)
    printf("%d ",res[i]);
    return 0;
}

*/

