    vector<int> tri_seq(n+1);
    tri_seq[0]=1;
    tri_seq[1]=3;
    tri_seq[2]=2;
    if (n>2){
        for (int i=3;i<=n;i++){
            if (i%2==0){
                tri_seq[i]=tri_seq[i-1]+tri_seq[i/2];
            }
            else{
                tri_seq[i]=tri_seq[i-1]+tri_seq[i-2]+tri_seq[i+1];
            }
        }
    }
    return tri_seq;
}



