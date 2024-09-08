    vector<string> result;

    sort(arr.begin(), arr.end());

    reverse(arr.begin(), arr.end());

    map<int, string> m = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};

    for(int i = 0; i < arr.size(); i++){
        if(m.count(arr[i])){
            result.push_back(m[arr[i]]);
        }
    }

    return result;
}

int main() {
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> result = by_length(arr);
    for(string s: result){
        cout << s << " ";
    }
    return 0;
}

