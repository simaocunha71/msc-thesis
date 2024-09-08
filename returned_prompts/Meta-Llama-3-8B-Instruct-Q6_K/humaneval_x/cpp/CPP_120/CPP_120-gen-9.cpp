    vector<int> result;
    sort(arr.begin(), arr.end(), greater<int>());
    for(int i = 0; i < k; i++){
        result.push_back(arr[i]);
    }
    return result;

}

int main(){
    vector<int> arr = {-3, -4, 5};
    int k = 3;
    vector<int> result = maximum(arr, k);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
