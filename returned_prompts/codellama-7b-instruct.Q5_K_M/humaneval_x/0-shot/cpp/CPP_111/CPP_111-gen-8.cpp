    map<char,int> h;
    char c;
    int count=0;
    for(int i=0;i<test.size();i++){
        c=test[i];
        count=0;
        for(int j=0;j<test.size();j++){
            if(c==test[j]){
                count++;
            }
        }
        h.insert(pair<char,int>(c,count));
    }
    return h;
}
