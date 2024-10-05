    int changes = 0;
    int n = arr.size();
    for(int i=0; i<n/2; i++){
        if(arr[i] != arr[n-i-1]){
            changes++;
        }
    }
    return changes;
}

int main() {
    vector<int> arr = {1, 2, 3, 2, 1};
    printf("%d", smallest_change(arr));
    return 0;
}
*/



/*
