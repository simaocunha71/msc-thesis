    int i;
    int frequency[100]={0};
    for(i=0;i<lst.size();i++){
        frequency[lst[i]]+=1;
    }
    for(i=lst.size()-1;i>=1;i--){
        if(frequency[i]>=i) return i;
    }
    return -1;
}


