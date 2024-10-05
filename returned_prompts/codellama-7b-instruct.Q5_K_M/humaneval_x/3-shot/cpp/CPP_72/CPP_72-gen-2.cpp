    int sum=0;
    bool balanced=true;
    for (int i=0;i<q.size();i++){
        if (q[i]!=q[q.size()-i-1])
        balanced=false;
        sum+=q[i];
    }
    if (sum>w)
    balanced=false;
    return balanced;
}


