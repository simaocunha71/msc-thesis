    int i,j,sum=0,max=0;
    for(i=0;i<lst.size();i++){
        for(j=2;j<=lst[i]/2;j++){
            if(lst[i]%j==0){
                break;
            }
        }
        if(lst[i]>1 && lst[i]>max && j>lst[i]/2){
            max=lst[i];
        }
    }
    if(max>0){
        string str = to_string(max);
        for(i=0; i<str.length(); i++){
            sum += str[i]-'0';
        }
    }
    return sum;
}

