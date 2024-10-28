    vector<int> res;
    for(int i=0; i<x.size(); i++){
        int num=x[i];
        bool flag = false;
        while(num>0){
            if((num%10)%2==0){
                flag = true;
                break;
            }
            num=num/10;
        }
        if(!flag){
            res.push_back(x[i]);
        }
    }
    sort(res.begin(), res.end());
    return res;
}


