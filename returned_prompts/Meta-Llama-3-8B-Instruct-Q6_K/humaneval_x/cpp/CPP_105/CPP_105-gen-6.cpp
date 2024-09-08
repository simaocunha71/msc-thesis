    map<int, string> m;
    m[1] = "One";
    m[2] = "Two";
    m[3] = "Three";
    m[4] = "Four";
    m[5] = "Five";
    m[6] = "Six";
    m[7] = "Seven";
    m[8] = "Eight";
    m[9] = "Nine";

    vector<string> result;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] >= 1 && arr[i] <= 9){
            result.push_back(m[arr[i]]);
        }
    }

    sort(result.begin(), result.end());
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> result = by_length(arr);
    for(auto i: result){
        cout << i << " ";
    }
    return 0;
}

