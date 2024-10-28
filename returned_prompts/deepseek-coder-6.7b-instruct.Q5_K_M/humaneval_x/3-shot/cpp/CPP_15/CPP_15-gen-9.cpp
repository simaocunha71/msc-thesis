    string sequence="";
    for(int i=0;i<=n;i++){
        sequence+=to_string(i);
        if(i<n){
            sequence+=" ";
        }
    }
    return sequence;
}


