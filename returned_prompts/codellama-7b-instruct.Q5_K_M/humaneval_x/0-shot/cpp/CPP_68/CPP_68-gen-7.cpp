    if(arr.size()==0)
        return {};
    vector<int> res;
    int sm_val=INT_MAX;
    int sm_ind=-1;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2==0){
            if(arr[i]<sm_val){
                sm_val=arr[i];
                sm_ind=i;
            }else if(arr[i]==sm_val){
                if(i<sm_ind)
                    sm_ind=i;
            }
        }
    }
    if(sm_val==INT_MAX)
        return {};
    res.push_back(sm_val);
    res.push_back(sm_ind);
    return res;
}
int main(){
    vector<int> arr={5, 0, 3, 0, 4, 2};
    vector<int> res=pluck(arr);
    for(int i=0;i<res.size();i++){
        printf("%d ",res[i]);
    }
    return 0;
}

