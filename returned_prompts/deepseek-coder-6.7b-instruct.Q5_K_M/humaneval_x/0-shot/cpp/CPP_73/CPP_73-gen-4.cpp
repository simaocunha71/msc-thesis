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
    vector<int> arr = {1,2,3,5,4,7,9,6};
    printf("%d\n", smallest_change(arr));
    return 0;
}
*/

