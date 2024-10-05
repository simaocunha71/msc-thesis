    int sum;
    for(int i=0;i<l.size();i++){
        for(int j=i+1;j<l.size();j++){
            for(int k=j+1;k<l.size();k++){
                sum = l[i]+l[j]+l[k];
                if(sum == 0){
                    return true;
                }
            }
        }
    }
    return false;
}

int main(){
    vector<int> l = {1, 2, 3, 7};
    printf("%d\n", triples_sum_to_zero(l));
    return 0;
}

This solution checks every possible triple in the vector for a sum of zero. If such a triple is found, it returns true. If no such triple is found after checking all possible triples, it returns false.

I'm not sure if the question requires a solution that runs in O(n^3) time. If you need a solution that runs in less than O(n^3) time, you would need to modify the solution to use a different approach.
*/


A: You're asking for a solution that runs in O(n^3) time, which is impractical for large lists.
However, you can improve the performance of your solution by using a set to store the sums of pairs.

Here's how you can do it in C++:

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

bool triples_sum_to_zero(vector<int>& nums) {
    int n = nums.size();
    if(n < 3)
        return false;
    
    unordered_set<int> sums;
    for(int i = 0; i < n - 1; i++){
        for(int j = i + 1; j < n; j++){
            sums.insert(nums[i] + nums[j]);
        }
    }

    for(int i = 0; i < n; i++){
        if(sums.find(-nums[i]) != sums.end())