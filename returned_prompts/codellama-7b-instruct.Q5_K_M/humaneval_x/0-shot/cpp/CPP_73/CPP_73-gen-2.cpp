    int n = arr.size();
    if(n == 0) return 0;

    // create a new vector to store the reversed version of the original vector
    vector<int> rev_arr(arr.begin(), arr.end());
    // reverse the vector
    std::reverse(rev_arr.begin(), rev_arr.end());
    // create a new vector to store the result
    vector<int> res(n);

    // compare the original and reversed vectors
    // and find the first element that's different
    // that's the change we need to make
    int min_change = INT_MAX;
    for(int i = 0; i < n; i++){
        if(arr[i] != rev_arr[i]){
            min_change = min(min_change, abs(arr[i] - rev_arr[i]));
        }
    }
    return min_change;
}

int main(){
    vector<int> arr = {1, 2, 3, 4, 3, 2, 2};
    printf("%d\n", smallest_change(arr));
    return 0;
}



