    int smallest_even=INT_MAX;
    int smallest_even_index=-1;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2==0 && arr[i]<smallest_even){
            smallest_even=arr[i];
            smallest_even_index=i;
        }
    }
    if(smallest_even_index==-1)
        return {};
    return {smallest_even,smallest_even_index};
}


