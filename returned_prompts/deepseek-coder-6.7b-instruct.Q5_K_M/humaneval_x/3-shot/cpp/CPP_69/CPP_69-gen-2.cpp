    int i,j,max=-1;
    for(i=0;i<lst.size();i++){
        int count=0;
        for(j=0;j<lst.size();j++){
            if(lst[i]==lst[j])
                count++;
        }
        if(count>=lst[i] && lst[i]>max)
            max=lst[i];
    }
    return max;
}


