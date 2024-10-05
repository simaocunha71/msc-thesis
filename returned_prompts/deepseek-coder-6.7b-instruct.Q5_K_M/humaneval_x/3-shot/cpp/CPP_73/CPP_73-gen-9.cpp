    int changes = 0;
    int len = arr.size();
    for(int i = 0; i < (len + 1) / 2; ++i){
        if(arr[i] != arr[len - 1 - i])
            changes++;
    }
    return changes;
}


