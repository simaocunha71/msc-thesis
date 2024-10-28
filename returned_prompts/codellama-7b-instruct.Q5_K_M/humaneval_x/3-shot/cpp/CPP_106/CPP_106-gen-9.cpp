    vector<int> result;
    int i,j;
    for (i=1;i<=n;i++){
        if (i%2==0)
        result.push_back(i);
        else{
            j=1;
            while (j<=i){
                result.push_back(j);
                j++;
            }
        }
    }
    return result;
}


