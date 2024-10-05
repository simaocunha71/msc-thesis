    if(arr.empty()){
        return -32768;
    }
    int sum = 0;
    int prod = 1;
    for(int i = 0; i < arr.size(); i++){
        int num = arr[i];
        if(num < 0){
            prod *= -1;
        }
        else if(num == 0){
            prod *= 0;
        }
        else{
            prod *= 1;
        }
        sum += abs(num);
    }
    return sum * prod;
}
