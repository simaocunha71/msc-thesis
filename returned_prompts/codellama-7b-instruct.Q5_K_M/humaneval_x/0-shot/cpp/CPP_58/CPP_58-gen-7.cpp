    vector<int> ans;
    int i=0,j=0;
    while(i<l1.size()&&j<l2.size()){
        if(l1[i]==l2[j]){
            ans.push_back(l1[i]);
            i++;
            j++;
        }
        else if(l1[i]<l2[j]) i++;
        else j++;
    }
    return ans;
}
int main(){
    vector<int> l1={1, 4, 3, 34, 653, 2, 5}, l2={5, 7, 1, 5, 9, 653, 121};
    vector<int> ans;
    ans=common(l1,l2);
    for(int i=0;i<ans.size();i++){
        printf("%d ",ans[i]);
    }
    return 0;
}
