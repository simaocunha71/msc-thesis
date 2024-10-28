    int sum=0;
    int i,j;
    for(i=0;i<q.size();i++){
        sum+=q[i];
        if(sum>w)
        return false;
    }
    if(sum==w){
        return true;
    }
    else{
        sum=0;
        for(j=q.size()-1;j>=0;j--){
            sum+=q[j];
            if(sum>w)
            return false;
        }
        if(sum==w)
        return true;
    }
    return false;
}


