    int sign = 1, sum = 0, product = 1;
    if(arr.empty())
        return -32768;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] < 0){
            sign *= -1;
            arr[i] = abs(arr[i]);
        }
        else if(arr[i] == 0)
            return 0;
        product *= arr[i];
    }
    sum = sign * product;
    return sum;
}

