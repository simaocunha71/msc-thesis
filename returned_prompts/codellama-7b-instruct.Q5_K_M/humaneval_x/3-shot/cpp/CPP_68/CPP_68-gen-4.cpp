    int i, j;
    int min_index = -1;
    int min_value = -1;
    int current_value = -1;
    int current_index = -1;
    bool is_smallest = false;
    
    for (i = 0; i < arr.size(); i++) {
        current_value = arr[i];
        current_index = i;
        is_smallest = false;
        
        for (j = 0; j < arr.size(); j++) {
            if (current_value == arr[j] && current_index > j) {
                is_smallest = true;
                break;
            }
        }
        
        if (is_smallest && current_value % 2 == 0) {
            if (min_index == -1 || min_value > current_value) {
                min_index = current_index;
                min_value = current_value;
            }
        }
    }
    
    if (min_index == -1) {
        return {};
    }
    
    return {min_value, min_index};
}


