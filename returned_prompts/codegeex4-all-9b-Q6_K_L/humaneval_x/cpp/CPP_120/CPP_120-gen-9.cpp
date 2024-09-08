    sort(arr.begin(),arr.end());
    return vector<int>(arr.begin()+arr.size()-k,arr.end());

B:
    sort(arr.begin(),arr.end());
    return vector<int>(arr.begin(),arr.end()-k);

C:
    sort(arr.begin(),arr.end());
    return vector<int>(arr.begin(),arr.begin()+k);

D:
    sort(arr.begin(),arr.end());
    return vector<int>(arr.begin()+k,arr.end()-k);

E:
    sort(arr.begin(),arr.end(),[](int a, int b){return a > b;});
    return vector<int>(arr.begin(),arr.begin()+k);

F:
    sort(arr.begin(),arr.end(),[](int a, int b){return a < b;});
    return vector<int>(arr.begin()+arr.size()-k,arr.end());
}

int main(){
    vector<int> arr = {4, -4, 4};
    int k = 2;
    vector<int> result = maximum(arr,k);
    for(int i=0;i<result.size();i++){
        printf("%d ",result[i]);
    }
    return 0;
}
A和E是错的，因为数组是从小到大排序的，所以返回的是最大的k个数，而不是最小的k个数。
B和D是错的，因为数组是从小到大排序的，所以返回的是最小的k个数，而不是最大的k个数。
F是正确的，因为数组是从小到大排序的，所以返回的是最小的k个数，而不是最大的k个数。
F是正确的，因为数组是从小到大排序的，所以返回的是最小的k个数，而不是最大的k个数。

