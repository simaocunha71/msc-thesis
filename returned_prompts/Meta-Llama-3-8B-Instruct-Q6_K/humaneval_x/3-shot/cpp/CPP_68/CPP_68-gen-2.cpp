    int min_even_index=-1;
    int min_even_value=INT_MAX;
    for (int i=0;i<arr.size();i++){
        if (arr[i]%2==0 && arr[i]<min_even_value){
            min_even_value=arr[i];
            min_even_index=i;
        }
    }
    if (min_even_index==-1)
        return {};
    else
        return {min_even_value, min_even_index};
}