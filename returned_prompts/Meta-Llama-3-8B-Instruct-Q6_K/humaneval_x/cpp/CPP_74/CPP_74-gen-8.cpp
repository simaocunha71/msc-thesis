    int sum1=0,sum2=0;
    for(int i=0;i<lst1.size();i++){
        sum1+=lst1[i].size();
    }
    for(int i=0;i<lst2.size();i++){
        sum2+=lst2[i].size();
    }
    if(sum1<sum2){
        return lst1;
    }
    else if(sum1>sum2){
        return lst2;
    }
    else{
        return lst1;
    }
}
