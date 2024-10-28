    int min_value=INT_MAX;
    int min_index=-1;
    for(int i=0;i<arr.size();i++){
        if(arr[i]<min_value && arr[i]%2==0){
            min_value=arr[i];
            min_index=i;
        }
    }
    if(min_index==-1)
        return {};
    else
        return {min_value, min_index};
}



