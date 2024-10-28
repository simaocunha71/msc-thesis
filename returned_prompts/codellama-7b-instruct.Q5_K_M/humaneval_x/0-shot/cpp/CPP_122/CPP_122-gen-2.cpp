    int sum = 0;
    int i = 0;
    while (i < k){
        if (arr[i] > 100){
            i++;
            continue;
        }
        sum += arr[i];
        i++;
    }
    return sum;
}

int main(){
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    printf("%d\n", add_elements(arr,k));
    return 0;
}
