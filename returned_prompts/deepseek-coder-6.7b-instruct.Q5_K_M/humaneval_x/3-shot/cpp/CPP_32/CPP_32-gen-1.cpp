    int i,j;
    double temp;
    for(i=0;i<xs.size();i++){
        if(xs[i]<0){
            xs[i]=-xs[i];
        }
    }
    for(i=0;i<xs.size()-1;i++){
        for(j=0;j<xs.size()-i-1;j++){
            if(xs[j]<xs[j+1]){
                temp=xs[j];
                xs[j]=xs[j+1];
                xs[j+1]=temp;
            }
        }
    }
    return xs[0]/xs[1];
}

