    sort(arr.begin(), arr.end(), [](int a, int b){
        int c = std::bitset<32>(a).count();
        int d = std::bitset<32>(b).count();
        return c < d || (c == d && a < b);
    });
    return arr;
}

int main(){
    vector<int> arr = {1, 5, 2, 3, 4};
    arr = sort_array(arr);
    for(int i=0; i<arr.size(); i++){
        printf("%d ",arr[i]);
    }
    return 0;
}
*/

