    vector<int> res;
    for(int num : x){
        bool flag = true;
        for(int i = 0; i < to_string(num).size(); i++){
            if(stoi(string(1, to_string(num)[i])) % 2 == 0){
                flag = false;
                break;
            }
        }
        if(flag) res.push_back(num);
    }
    sort(res.begin(), res.end());
    return res;
}

int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> result = unique_digits(x);
    for(int num : result) printf("%d ", num);
    printf("\n");
    return 0;
}
