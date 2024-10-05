    int i,j;
    for(i=lst.size()-1;i>=0;i--){
    int count=0;
    for(j=0;j<lst.size();j++){
    if(lst[j]==lst[i]){
    count++;
    }
    }
    if(count>=lst[i]){
    return lst[i];
    }
    }
    return -1;
}

