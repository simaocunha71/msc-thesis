    sort(arr.begin(), arr.end(),[](int a, int b){
        int count_a = __builtin_popcount(abs(a));
        int count_b = __builtin_popcount(abs(b));
        return count_a < count_b || (count_a == count_b && a < b);
    });
    return arr;
}

int main()
{
    vector<int> arr = {1, 5, 2, 3, 4};
    vector<int> sorted_arr = sort_array(arr);
    for(int i = 0; i < sorted_arr.size(); i++){
        printf("%d ", sorted_arr[i]);
    }
    return 0;
}

*/

#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> sort_vector(vector<int> arr){
    // Implement your solution here
    sort(arr.begin(), arr.end(), [](int a, int b){
        int count_a = __builtin_popcount(abs(a));
        int count_b = __builtin_popcount(abs(b));
        return count_a < count_b || (count_a == count_b && a < b);
    });
    return arr;
}

int main()
{
    vector<int> arr = {1, 5, 2, 3, 4};
    vector<int> sorted_arr = sort_vector(arr);
    for(int i = 0; i < sorted_arr.size(); i++){
        printf("%d ", sorted_arr[i]);
    }
    return 0;
}

