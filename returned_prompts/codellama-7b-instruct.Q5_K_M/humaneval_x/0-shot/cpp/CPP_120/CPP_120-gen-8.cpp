    if(k==0){
        return {};
    }
    if(k==1){
        vector<int> ans;
        ans.push_back(arr[0]);
        return ans;
    }
    vector<int> ans;
    int max=arr[0];
    for(auto i:arr){
        if(i>max){
            max=i;
        }
    }
    for(int i=0;i<arr.size();i++){
        if(arr[i]==max){
            arr.erase(arr.begin()+i);
            i--;
        }
    }
    ans.push_back(max);
    k--;
    if(k==0){
        return ans;
    }
    goto A;
}
int main(){
    vector<int> arr={-3, -4, 5};
    vector<int> ans=maximum(arr,3);
    for(auto i:ans){
        printf("%d ",i);
    }
    return 0;
}
