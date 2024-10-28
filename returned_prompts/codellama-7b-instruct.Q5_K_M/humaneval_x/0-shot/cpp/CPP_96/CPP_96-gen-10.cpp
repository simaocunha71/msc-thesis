    vector<int> a;
    for(int i=0;i<n;i++){
        if(i==0){
            a.push_back(i);
        }
        else{
            if(i==1){
                a.push_back(i);
            }
            else{
                if(i%2==0){
                    a.push_back(i);
                }
                else{
                    a.push_back(i);
                }
            }
        }
    }
    return a;
}
