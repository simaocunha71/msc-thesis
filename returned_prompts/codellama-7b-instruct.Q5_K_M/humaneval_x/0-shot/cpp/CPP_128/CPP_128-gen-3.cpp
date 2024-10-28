    int n = arr.size();
    if(n == 0){
        return -32768;
    }
    int prod = 1;
    int sum = 0;
    for(int i = 0; i < n; i++){
        if(arr[i] == 0){
            continue;
        }
        else if(arr[i] < 0){
            prod *= -1;
        }
        else{
            prod *= 1;
        }
        sum += abs(arr[i]);
    }
    return prod * sum;
}

B:
    int n = arr.size();
    if(n == 0){
        return -32768;
    }
    int prod = 1;
    int sum = 0;
    for(int i = 0; i < n; i++){
        if(arr[i] == 0){
            continue;
        }
        else if(arr[i] < 0){
            prod *= -1;
        }
        else{
            prod *= 1;
        }
        sum += abs(arr[i]);
    }
    return prod * sum;
}
