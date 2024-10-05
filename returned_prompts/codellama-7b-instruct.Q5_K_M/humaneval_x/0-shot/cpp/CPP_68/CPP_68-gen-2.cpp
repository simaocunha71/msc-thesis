    if(arr.size()==0)
        return {};
    int min_val = INT_MAX;
    int min_index = 0;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2==0&&arr[i]<min_val){
            min_val = arr[i];
            min_index = i;
        }
    }
    if(min_val==INT_MAX)
        return {};
    vector<int> ans;
    ans.push_back(min_val);
    ans.push_back(min_index);
    return ans;
}
int main(){
    vector<int> arr = {1,2,3};
    vector<int> res = pluck(arr);
    for(auto x: res)
        printf("%d ",x);
    printf("\n");
    return 0;
}
