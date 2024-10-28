    int smallest_even = INT_MAX;
    int smallest_even_index = -1;
    for (int i = 0; i < arr.size(); i++){
        if (arr[i] < smallest_even && arr[i] % 2 == 0){
            smallest_even = arr[i];
            smallest_even_index = i;
        }
    }
    if (smallest_even == INT_MAX){
        return {};
    }
    else{
        return {smallest_even, smallest_even_index};
    }

}

