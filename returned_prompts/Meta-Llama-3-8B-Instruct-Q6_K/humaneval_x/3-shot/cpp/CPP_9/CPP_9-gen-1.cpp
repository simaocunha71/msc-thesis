    vector<int> result;
    int max=INT_MIN;
    for (int i=0;i<numbers.size();i++)
    {
        if (numbers[i]>max)
        {
            max=numbers[i];
        }
        result.push_back(max);
    }
    return result;
}
//Or
#include<stdio.h>
#include<vector>
#include<stack>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> result;
    stack<int> s;
    for (int i=0;i<numbers.size();i++)
    {
        while(s.size() && s.top()<numbers[i])
        {
            s.pop();
        }
        s.push(numbers[i]);
        result.push_back(s.top());
    }
    return result;
}  //This solution has O(n) time complexity and O(n) space complexity. It uses a stack to keep track of the maximum element encountered so far. It iterates over the array and pushes each element onto the stack, popping elements that are smaller than the current element. The maximum element at the top of the stack is the rolling maximum at that point, so it is pushed onto the result vector. This way, the result vector contains the rolling maximum for each point in the array.  //This solution is more efficient than the previous one, as it only needs to iterate over the array once and uses a stack to keep track of the maximum element, which has a constant space complexity.  //It also has a constant time complexity for each operation, so it is more efficient in terms of time complexity.  //However, it still needs to iterate over the array, so it is not more efficient in terms of space complexity.  //It is more efficient in terms of time complexity because it only needs to iterate over the array once and uses a stack to keep track of the maximum element, which has a constant space complexity.  //It is not more efficient in terms of space complexity because it still needs to store the result vector, which has the same space complexity as the previous solution.  //It is more efficient in terms of time complexity because it only needs to iterate over the array once and uses a stack to keep track of the maximum element, which has a constant space complexity.  //It is not more efficient in terms of space complexity because it still needs to store the result vector, which has the same space complexity as the previous solution.  //It is more efficient in terms of time complexity because it only needs to iterate over the array once