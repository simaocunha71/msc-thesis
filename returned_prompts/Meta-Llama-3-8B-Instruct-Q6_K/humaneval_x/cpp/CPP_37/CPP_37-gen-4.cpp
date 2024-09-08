    vector<float> l;
    for(int i=0; i<5; i++){
        l.push_back(i);
    }
    vector<float> l1;
    for(int i=0; i<l.size(); i++){
        if(i%2==0){
            l1.push_back(l[i]);
        }
    }
    sort(l1.begin(), l1.end());
    int j=0;
    for(int i=0; i<l.size(); i++){
        if(i%2==0){
            l[i] = l1[j];
            j++;
        }
    }
    return l;
}

