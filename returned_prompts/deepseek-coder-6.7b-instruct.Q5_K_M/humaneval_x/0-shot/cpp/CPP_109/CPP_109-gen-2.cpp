    int n = arr.size();
    if(n == 0) return true;
    int count = 0;

B:
    for(int i = 0; i < n - 1; i++){
        if(arr[i] > arr[i+1]){
            count++;
        }
    }
