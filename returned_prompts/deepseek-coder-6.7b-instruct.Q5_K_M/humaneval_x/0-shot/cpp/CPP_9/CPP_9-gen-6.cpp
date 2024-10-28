vector<int> res;
int max= numbers[0];
res.push_back(max);
for(int i=1;i<numbers.size();i++){
    if(numbers[i]>max){
        max=numbers[i];
    }
    res.push_back(max);
}
return res;
}

int main() {
    vector<int> numbers= {1, 2, 3, 2, 3, 4, 2};
    vector<int> res= rolling_max(numbers);
    for(int i=0; i<res.size();i++){
        printf("%d ",res[i]);
    }
    return 0;
}

*/

#include <iostream>
#include <vector>
using namespace std;

vector<int> rolling_max(vector<int> numbers)
{
    vector<int> result;
    int max_value = numbers[0];
    result.push_back(max_value);

    for (int i = 1; i < numbers.size(); i++)
    {
        if (numbers[i] > max_value)
        {
            max_value = numbers[i];
        }
        result.push_back(max_value);
    }

    return result;
}

int main()
{
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> result = rolling_max(numbers);

    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }

    return 0;
}

// Output: 1 2 3 3 3 4 4 

// Explanation: At the first moment, the maximum value is 1. After that, the maximum values are 2, 3, 3, 3, 4, 4, 4.
// For each index in the vector, it keeps track of the maximum value found so far.

// Time complexity: O(n)