    int i;
    int m;
    vector<int> v;
    v.push_back(numbers[0]);
    for(i=1; i<numbers.size(); i++){
        if(numbers[i]>numbers[i-1]){
            v.push_back(numbers[i]);
        }else{
            v.push_back(m);
        }
    }
    return v;
}


