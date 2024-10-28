    vector<int> res;
    for(auto i: x){
        int num=i;
        bool flag=false;
        while(num){
            if((num%10)%2==0){
                flag=true;
                break;
            }
            num/=10;
        }
        if(!flag)
            res.push_back(i);
    }
    sort(res.begin(),res.end());
    return res;
}

int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> res = unique_digits(x);
    for(auto i: res)
        printf("%d ", i);
    return 0;
}

//C++ Program/unique_digits_v2.cpp
