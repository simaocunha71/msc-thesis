    sort(arr.begin(),arr.end());
    int n = arr.size();
    vector<int> res(k);
    for(int i = 0;i < k;i++) res[i] = arr[n-i-1];
    return res;
}

int main(){
    vector<int> arr = {-3,-4,5};
    int k = 3;
    vector<int> res = maximum(arr,k);
    for(int i = 0;i < res.size();i++) printf("%d ",res[i]);
    printf("\n");

    vector<int> arr2 = {4,-4,4};
    int k2 = 2;
    vector<int> res2 = maximum(arr2,k2);
    for(int i = 0;i < res2.size();i++) printf("%d ",res2[i]);
    printf("\n");

    vector<int> arr3 = {-3,2,1,2,-1,-2,1};
    int k3 = 1;
    vector<int> res3 = maximum(arr3,k3);
    for(int i = 0;i < res3.size();i++) printf("%d ",res3[i]);
    printf("\n");

    return 0;
}



























*/









































































































































































