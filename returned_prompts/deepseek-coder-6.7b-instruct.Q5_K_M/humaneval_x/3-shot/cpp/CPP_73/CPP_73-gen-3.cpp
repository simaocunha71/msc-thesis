    int changes = 0;
    int i = 0;
    int j = arr.size()-1;
    while(i<j){
        if(arr[i] != arr[j]){
            changes++;
        }
        i++;
        j--;
    }
    return changes;
}


