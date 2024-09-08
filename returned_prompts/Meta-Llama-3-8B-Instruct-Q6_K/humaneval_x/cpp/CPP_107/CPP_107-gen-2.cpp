    vector<int> res(2, 0);
    for(int i = 1; i <= n; i++){
        string s = to_string(i);
        bool is_palindrome = true;
        for(int j = 0; j < s.length(); j++){
            if(s[j] != s[s.length() - j - 1]){
                is_palindrome = false;
                break;
            }
        }
        if(is_palindrome && i % 2 == 0) res[0]++;
        else if(is_palindrome) res[1]++;
    }
    return res;
}

int main(){
    int n;
    cin >> n;
    vector<int> res = even_odd_palindrome(n);
    cout << "(" << res[0] << ", " << res[1] << ")" << endl;
    return 0;
}

// Time complexity: O(n log n)
// Space complexity: O(n) for the vector and string objects

// The time complexity is O(n log n) because for each integer from 1 to n, we
// are converting it to a string and then checking if it's a palindrome, which
// takes O(log n) time. So the overall time complexity is O(n log n).

// The space complexity is O(n) because we are using a vector of size n and
// for each integer from 1 to n, we are creating a string object of size log n. So
// the overall space complexity is O(n).