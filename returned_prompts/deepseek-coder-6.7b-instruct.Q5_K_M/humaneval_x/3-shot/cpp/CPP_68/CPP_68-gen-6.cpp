    vector<int> ans;
    int smallest = 2147483647;
    int index = -1;
    for(int i=0; i<arr.size(); i++){
        if(arr[i]<smallest && arr[i]%2 == 0){
            smallest = arr[i];
            index = i;
        }
    }
    if(index != -1){
        ans.push_back(smallest);
        ans.push_back(index);
    }
    return ans;
}


