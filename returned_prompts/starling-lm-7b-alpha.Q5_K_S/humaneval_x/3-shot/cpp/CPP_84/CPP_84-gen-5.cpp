    string bin="";
    int tmp=N;
    while (tmp>0){
        bin=std::to_string(tmp%2)+bin;
        tmp/=2;
    }
    int sum=0;
    for (int i=0;i<bin.length();i++)
    sum+=(bin[i]-'0');
    return std::to_string(sum);
}


