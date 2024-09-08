    sort(arr.begin(), arr.end());
    return vector<int>(arr.begin(), arr.begin() + k);
}

int main(){
    vector<int> arr = {-3, -4, 5};
    int k = 3;
    vector<int> result = maximum(arr,k);
    for(int i = 0; i < k; i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

