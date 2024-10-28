    int i,j,max=-1;
    int count;
    for  (i=1;i<=100;i++){
        count=0;
        for  (j=0;j<lst.size();j++){
            if  (lst[j]==i){
                count+=1;
            }
        }
        if  (count>=i && i>max){
            max=i;
        }
    }
    return max;
}


