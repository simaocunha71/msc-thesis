#include <iostream>
using namespace std;
#include <vector>
bool pairs_sum_to_zero(vector<int> arr){
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] == 0) {
                return true;
            }
        }
    }
    return false;
}
int main(){
    vector<int> arr = {1, 2, 3, 4, 5};
    cout << pairs_sum_to_zero(arr) << endl;
    return 0;
}

B:
#include <iostream>
#include <vector>
using namespace std;
bool pairs_sum_to_zero(vector<int> arr){
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] == 0) {
                return true;
            }
        }
    }
    return false;
}
int main(){
    vector<int> arr = {1, 2, 3, 4, 5};
    cout << pairs_sum_to_zero(arr) << endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
using namespace std;
bool pairs_sum_to_zero(vector<int> arr){
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] == 0) {
                return true;
            }
        }
    }
    return false;
}
int main(){
    vector<int> arr = {1, 2, 3, 4, 5};
    cout << pairs_sum_to_zero(arr) << endl;
    return 0;
}

D:
#include <iostream>
#include <vector>
using namespace std;
bool pairs_sum_to_zero(vector<int> arr){
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] == 0) {
                return true;
            }
        }
    }
   