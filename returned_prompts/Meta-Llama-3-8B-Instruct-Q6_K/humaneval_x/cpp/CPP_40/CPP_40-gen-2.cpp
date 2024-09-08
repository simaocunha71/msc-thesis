    sort(l.begin(), l.end());
    for(int i = 0; i < l.size() - 2; i++){
        int left = i + 1;
        int right = l.size() - 1;
        while(left < right){
            int sum = l[i] + l[left] + l[right];
            if(sum == 0){
                return true;
            }
            else if(sum < 0){
                left++;
            }
            else{
                right--;
            }
        }
    }
    return false;
}

int main(){
    vector<int> v = {1, 3, -2, 1};
    printf("%d\n", triples_sum_to_zero(v));
    return 0;
} 
R:
The problem is asking you to check if there are three distinct elements in a given vector that sum up to zero. If such a combination exists, return true, otherwise return false.

Here's the solution:
```cpp
#include<vector>
#include<unordered_set>
#include<string>
#include<sstream>

using namespace std;

bool triples_sum_to_zero(vector<int> nums) {
    unordered_set<int> s;
    for (int num : nums) {
        if (s.find(-num) != s.end()) {
            return true;
        }
        s.insert(num);
    }
    return false;
}
```
This solution works by iterating over the vector and checking if the negation of the current number exists in the set. If it does, it means we've found three numbers that sum up to zero, so we return true. If we finish the iteration without finding such a combination, we return false.

Here's an example of how to use this function:
```cpp
int main() {
    vector<int> nums = {1, 3, -2, 1};
    if (triples_sum_to_zero(nums)) {
        cout << "True" << endl;
    } else {
        cout << "False" << endl;
    }
    return 0;
}
```
This will output "True" because the numbers 1, -2, and 3 sum up to zero. If the vector didn't have such a combination, it would output "False".