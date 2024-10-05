    vector<int> y;
    for (int i=0;i<x.size();i++)
    {
        int j;
        for (j=1;j<10;j++)
        if ((x[i]%j)==0){
            if (j%2!=0)
            y.push_back(x[i]);
            break;
        }
    }
    sort(y.begin(), y.end());
    return y;
}


