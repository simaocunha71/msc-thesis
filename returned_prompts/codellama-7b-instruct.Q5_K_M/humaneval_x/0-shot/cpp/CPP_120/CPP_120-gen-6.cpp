    sort(arr.begin(),arr.end());

B:
    vector<int> result;
    for(int i=arr.size()-1;i>=0;i--){
        result.push_back(arr[i]);
        if(result.size()==k) break;
    }
    reverse(result.begin(),result.end());
    return result;
}
int main(){
    vector<int> arr;
    int k;
    arr.push_back(-3);
    arr.push_back(-4);
    arr