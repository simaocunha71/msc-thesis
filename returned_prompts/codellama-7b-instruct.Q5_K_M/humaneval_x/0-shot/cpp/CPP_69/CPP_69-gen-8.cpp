    int max=0;
    for(int i=0; i<lst.size(); i++){
        if(lst[i]>max){
            max=lst[i];
        }
    }
    for(int i=0; i<lst.size(); i++){
        int cnt=1;
        for(int j=i+1; j<lst.size(); j++){
            if(lst[j]==lst[i])