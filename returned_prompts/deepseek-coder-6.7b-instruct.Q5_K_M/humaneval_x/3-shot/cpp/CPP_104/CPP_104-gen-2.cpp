    vector<int> result;
    for(int i=0; i<x.size(); i++){
        int num = x[i];
        bool isUnique = true;
        while(num > 0){
            if((num%10)%2 == 0){
                isUnique = false;
                break;
            }
            num /= 10;
        }
        if(isUnique){
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

