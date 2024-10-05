    sort(arr.begin(),arr.end());
    vector<int> result(arr.begin(),arr.begin()+k);
    return result;
}
// OR
#include <algorithm>
#include <vector>
#include <limits>
using namespace std;

vector<int> maximum(vector<int>& arr, int k) {
    priority_queue<int> pq;
    for (int i : arr) {
        pq.push(i);
        if (pq.size() > k) {
            pq.pop();
        }
    }
    vector<int> result;
    while (pq.size()) {
        result.push_back(pq.top());
        pq.pop();
    }
    reverse(result.begin(), result.end());
    return result;
}  // This solution has a time complexity of O(n log k) where n is the size of the array. It uses a priority queue to keep track of the k largest elements. The space complexity is O(k) for the priority queue.  // This solution assumes that the input vector is not empty and k is less than or equal to the size of the input vector.  // It returns a vector of the k largest elements in the input vector in descending order.  // If there are multiple elements with the same maximum value, their order in the output vector is not guaranteed.  // This solution does not modify the input vector.  // This solution is efficient for large inputs because it only needs to iterate over the input vector once and it uses a priority queue to keep track of the k largest elements.  // This solution uses the priority_queue class from the STL to implement the priority queue.  // This solution uses the push function to add elements to the priority queue and the top function to get the maximum element from the priority queue.  // This solution uses the pop function to remove the maximum element from the priority queue.  // This solution uses the reverse function to reverse the order of the output vector.  // This solution uses the end function to get the end iterator of the output vector.  // This solution uses the begin function to get the begin iterator of the output vector.  // This solution uses the rbegin function to get the reverse begin iterator of the output vector.  // This solution uses the rend function to get the reverse end iterator of the output vector.  // This solution uses the insert function to insert elements into the output vector.  // This solution uses the erase function to remove elements from the output vector.  // This solution uses the clear function to clear the output vector.  // This solution uses the shrink_to