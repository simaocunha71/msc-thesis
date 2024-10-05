    int i,j,count=0;
    for(i=0,j=arr.size()-1;i<j;i++,j--){
        if(arr[i] != arr[j]) count++;
    }
    return count;
}


