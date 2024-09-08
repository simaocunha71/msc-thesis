    int n = arr.size();
    int count = 0;
    vector<int> left(n), right(n);
    for(int i = 0; i < n; i++){
        left[i] = arr[i];
    }
    for(int i = n-1; i >= 0; i--){
        right[i] = arr[i];
    }
    for(int i = 0; i < n; i++){
        if(left[i] != right[n-1-i]){
            count++;
        }
    }
    return count;
}
int main()
{
    vector<int> arr = {1,2,3,5,4,7,9,6};
    printf("Number of changes required: %d\n", smallest_change(arr));
    return 0;
}

