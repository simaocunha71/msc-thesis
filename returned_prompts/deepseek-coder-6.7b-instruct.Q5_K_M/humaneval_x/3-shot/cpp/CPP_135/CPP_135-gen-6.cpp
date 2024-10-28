    int max_index = -1;
    for(int i = arr.size()-1; i > 0; i--){
        if(arr[i] < arr[i-1]){
            max_index = i;
            break;
        }
    }
    return max_index;
}


