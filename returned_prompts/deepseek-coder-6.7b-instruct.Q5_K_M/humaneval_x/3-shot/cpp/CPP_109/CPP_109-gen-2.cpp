    int n = arr.size();
    if(n == 0)
        return true;
    int count = 0;
    for(int i = 0; i < n - 1; i++){
        if(arr[i] > arr[i + 1])
            count++;
    }
    if(arr[n - 1] > arr[0])
        count++;
    return count <= 1;
}


