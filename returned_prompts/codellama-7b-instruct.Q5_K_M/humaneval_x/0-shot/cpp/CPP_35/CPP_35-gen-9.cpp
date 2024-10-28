    if(l.size() == 1){
        return l[0];
    }
    else{
        vector<float> l1;
        for(int i = 1; i < l.size(); i++){
            if(l[i] > l[0]){
                l1.push_back(l[i]);
            }
        }
        l = l1;
        goto A;
    }
}
