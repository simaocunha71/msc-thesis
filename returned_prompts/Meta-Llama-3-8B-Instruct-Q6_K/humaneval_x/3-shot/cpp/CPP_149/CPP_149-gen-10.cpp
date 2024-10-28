    vector<string> result;
    for (int i=0; i<lst.size(); i++){
        if (lst[i].length() % 2 == 0){
            result.push_back(lst[i]);
        }
    }
    sort(result.begin(), result.end(), [](string a, string b) {
        if (a.length() == b.length()) {
            return a < b;
        }
        return a.length() < b.length();
    });
    return result;
} // end of function
int main() {
    vector<string> lst = {"aa", "a", "aaa"};
    vector<string> result = sorted_list_sum(lst);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    return 0;
} // end of main
// Output: "aa" 
// This is the expected output
// The function sorted_list_sum removes the strings with odd lengths and sorts the remaining strings by their lengths and then alphabetically.
// The function is tested in the main function with the input vector {"aa", "a", "aaa"}. The output is "aa", which is the expected result.