    int n = arr.size();
    int ans = 0;
    for(int i = 0; i < n; i++){
        if(arr[i] != arr[n - i - 1]){
            ans++;
        }
    }
    return ans;
}

// 
// int main(){
//     vector<int> v = {1, 2, 3, 4, 3, 2, 2};
//     int ans = smallest_change(v);
//     cout << ans << endl;
// }
