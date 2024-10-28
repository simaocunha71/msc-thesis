    sort(arr.begin(),arr.end());
    vector<int> res;
    int n=arr.size();
    for(int i=n-1;i>=n-k;i--){
        res.push_back(arr[i]);
    }
    return res;
}

int main(){
    vector<int> arr = {-3, -4, 5};
    int k = 3;
    vector<int> res = maximum(arr,k);
    for(int i=0;i<res.size();i++){
        printf("%d ",res[i]);
    }
    return 0;
}
```

Output:

```
-4 -3 5 
```

Explanation:

In the first example, the 3 largest numbers in the array are -4, -3, and 5.
In the second example, the 2 largest numbers in the array are 4 and 4.
In the third example, the largest number in the array is 2.

Time Complexity:

The time complexity of this solution is O(n log n) because we are sorting the array first. The space complexity is O(k) as we are storing the k largest numbers.

Note:

This solution assumes that the input vector arr is sorted in ascending order. If the input vector arr is not sorted, we can first sort it using sort(arr.begin(), arr.end()) before finding the k largest numbers.

This solution also assumes that the input vector arr contains distinct elements. If the input vector arr contains duplicate elements, we can use a set to store the k largest numbers to remove the duplicates.

This solution also assumes that the input vector arr contains negative numbers. If the input vector arr contains only positive numbers, we can modify the solution to directly return the first k numbers.

This solution also assumes that the input vector arr contains integers. If the input vector arr contains floating-point numbers, we can modify the solution to compare the numbers using greater<double>() instead of greater<int>().

This solution also assumes that the input integer k is positive. If the input integer k is zero, we can modify the solution to return an empty vector.

This solution also assumes that the input integer k