#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

vector<string> by_length(vector<int> arr){
    vector<int> sorted_arr;
    vector<string> sorted_arr_str;

    map<int,string> digit_to_word = {
        {1,"One"}, {2,"Two"}, {3,"Three"}, {4,"Four"}, {5,"Five"},
        {6,"Six"}, {7,"Seven"}, {8,"Eight"}, {9,"Nine"}
    };

    // sort the arr
    sort(arr.begin(), arr.end());

    // reverse the arr
    reverse(arr.begin(), arr.end());

    // filter out the elements not in the range [1,9]
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] >= 1 && arr[i] <= 9) {
            sorted_arr.push_back(arr[i]);
        }
    }

    // convert the sorted_arr to sorted_arr_str
    for (int i = 0; i < sorted_arr.size(); i++) {
        sorted_arr_str.push_back(digit_to_word[sorted_arr[i]]);
    }

    return sorted_arr_str;
}

int main() {
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> result = by_length(arr);
    for (int i = 0; i < result.size(); i++) {
        printf("%s ", result[i].c_str());
    }
    printf("\n");
    return 0;
}

C:
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

vector<string> by_length(vector<int> arr){
    vector<int> sorted_arr;
    vector<string> sorted_arr_str;

    map<int,string> digit_to_word = {
        {1,"One"}, {2,"Two"}, {3,"Three"}, {4,"Four"}, {5,"Five"},
        {6,"Six"}, {7,"Seven"}, {8,"Eight"}, {9,"Nine"}
    };

    // sort the arr
    sort(arr.begin(), arr.end());

    // reverse the arr
    reverse(arr.begin(), arr.end());

    // filter out the elements not in the range [1,9]
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] >= 1 && arr[i] <=