    map<int, string> m;
    m[1]="One";
    m[2]="Two";
    m[3]="Three";
    m[4]="Four";
    m[5]="Five";
    m[6]="Six";
    m[7]="Seven";
    m[8]="Eight";
    m[9]="Nine";
    vector<string> result;
    vector<int> num_arr;
    for (int i=0;i<arr.size();i++){
        if (arr[i]>=1 && arr[i]<=9){
            num_arr.push_back(arr[i]);
        }
    }
    sort(num_arr.begin(),num_arr.end());
    reverse(num_arr.begin(),num_arr.end());
    for (int i=0;i<num_arr.size();i++){
        result.push_back(m[num_arr[i]]);
    }
    return result;
}
// Test case
int main() {
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> result = by_length(arr);
    for (int i=0;i<result.size();i++){
        cout<<result[i]<<" ";
    }
    return 0;
}
