    vector<int> vec;
    if(arr.size() == 0)
        return vec;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0){
            vec.push_back(arr[i]);
            vec.push_back(i);
            break;
        }
    }
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0){
            for(int j = i+1; j < arr.size(); j++){
                if(arr[j] % 2 == 0){
                    if(arr[j] < vec[0]){
                        vec[0] = arr[j];
                        vec[1] = j;
                    }
                }
            }
        }
    }
    for(int i = 0; i < vec.size(); i++){
        printf("%d ", vec[i]);
    }
    return vec;
}
int main(){
    vector<int> arr{4,2,3};
    vector<int> ans = pluck(arr);
    for(int i = 0; i < ans.size(); i++){
        printf("%d ", ans[i]);
    }
    return 0;
}
