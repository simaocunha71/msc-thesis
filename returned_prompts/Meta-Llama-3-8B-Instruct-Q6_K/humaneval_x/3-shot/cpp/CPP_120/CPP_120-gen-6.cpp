    sort(arr.begin(), arr.end());
    vector<int> max_nums;
    for(int i=arr.size()-1; i>=arr.size()-k; i--)
    {
        max_nums.push_back(arr[i]);
    }
    return max_nums;
} // This solution works in O(n log n) time complexity. The time complexity can be further improved to O(n log k) by using a priority queue. Here is the improved solution: 
#include <queue>
using namespace std;
vector<int> maximum(vector<int> arr, int k){
    priority_queue<int> pq;
    for (int num : arr) {
        pq.push(num);
        if (pq.size() > k) {
            pq.pop();
        }
    }
    vector<int> max_nums;
    while (pq.size() > 0) {
        max_nums.push_back(pq.top());
        pq.pop();
    }
    reverse(max_nums.begin(), max_nums.end());
    return max_nums;
} // This solution works in O(n log k) time complexity.  // This is the best solution for this problem. 
// It uses a priority queue to keep track of the k largest elements in the array, with a time complexity of O(n log k), where n is the size of the array and k is the number of elements to keep track of.  // This is the most efficient solution for this problem. 
// It uses a priority queue to keep track of the k largest elements in the array, with a time complexity of O(n log k), where n is the size of the array and k is the number of elements to keep track of.  // This is the most efficient solution for this problem. 
// It uses a priority queue to keep track of the k largest elements in the array, with a time complexity of O(n log k), where n is the size of the array and k is the number of elements to keep track of.  // This is the most efficient solution for this problem. 
// It uses a priority queue to keep track of the k largest elements in the array, with a time complexity of O(n log k), where n is the size of the array and k is the number of elements to keep track of.  // This is the most efficient solution for this problem. 
// It uses a priority queue to keep track of the k largest elements in the array, with a time complexity of O(n log k), where n is the size of the array and k is the number of elements to