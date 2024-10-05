    int i;
    int n=lst.size();
    for(i=n-1;i>=0;i--){
        int count=0;
        int current=lst[i];
        for(int j=0;j<n;j++){
            if(lst[j]==current)
                count++;
        }
        if(count>=current)
            return current;
    }
    return -1;
}

