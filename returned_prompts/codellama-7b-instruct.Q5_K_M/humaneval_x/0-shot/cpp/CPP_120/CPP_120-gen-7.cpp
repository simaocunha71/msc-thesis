    vector<int> ans;
    vector<int> tmp;
    sort(arr.begin(),arr.end());
    for(int i = 0;i<k;i++){
        tmp.push_back(arr.back());
        arr.pop_back();
    }
    ans = tmp;
    return ans;
}
int main(){
    vector<int> vec;
    vec.push_back(4);
    vec.push_back(-4);
    vec.push_back(4);
    vector<int> ans = maximum(vec,2);
    for(int i = 0;i<ans.size();i++){
        printf("%d ",ans[i]);
    }
    return 0;
}
