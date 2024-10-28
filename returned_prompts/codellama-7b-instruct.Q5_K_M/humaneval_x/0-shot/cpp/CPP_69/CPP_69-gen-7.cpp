    int n = lst.size();
    int mx = 0;
    for(int i = 0; i < n; i++){
        if(lst[i] > mx){
            mx = lst[i];
        }
    }
    int ans = -1;
    for(int i = 0; i < n; i++){
        if(lst[i] == mx && lst[i] >= mx){
            ans = lst[i];
            break;
        }
    }
    return ans;
}
int main(){
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    printf("%d\n", search(lst));
    return 0;
}
