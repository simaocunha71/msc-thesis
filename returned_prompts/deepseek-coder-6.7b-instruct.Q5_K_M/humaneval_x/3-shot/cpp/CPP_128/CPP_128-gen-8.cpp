    if(arr.empty())
        return -32768;
    int sum = 0;
    int prod = 1;
    for(int i=0; i<arr.size(); i++){
        if(arr[i] > 0){
            sum += abs(arr[i]);
            prod *= 1;
        }
        else if(arr[i] < 0){
            sum += abs(arr[i]);
            prod *= -1;
        }
        else if(arr[i] == 0){
            return 0;
        }
    }
    return prod*sum;
}


