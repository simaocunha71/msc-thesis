    vector<int> res;
    int n = arr.size();
    if(n == 0 || k == 0) return res;
    sort(arr.begin(),arr.end());
    for(int i = n - k; i < n; i++){
        res.push_back(arr[i]);
    }
    return res;

}
int main(void){
    vector<int> res = maximum({-3, -4, 5}, 3);
    for(auto i : res){
        printf("%d ",i);
    }
    printf("\n");
}
