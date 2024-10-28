    sort(arr.begin(),arr.end());
    vector<int> res;
    for(int i = arr.size()-1; i>=arr.size()-k; --i)
    {
        res.push_back(arr[i]);
    }
    return res;
}

int main()
{
    vector<int> arr;
    int k;
    arr.push_back(-3);
    arr.push_back(-4);
    arr.push_back(5);
    k = 3;
    vector<int> res = maximum(arr, k);
    for(int i=0; i<res.size(); i++)
    {
        printf("%d ",res[i]);
    }
    return 0;
}

This C++ code does not handle the case where k is larger than the number of distinct elements in arr. It assumes that k is less than or equal to the length of arr. If k is larger than the number of elements in arr, it would return an empty vector.
*/

//Python code:
def maximum(arr, k):
    arr.sort()
    return arr[-k:]

print(maximum([-3, -4, 5], 3))
print(maximum([4, -4, 4], 2))
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))

#This Python code will handle the case where k is larger than the number of distinct elements in arr by returning the k largest distinct elements in arr.
#If k is equal to the number of distinct elements in arr, it will return all the distinct elements in arr.
#If k is less than the number of distinct elements in arr, it will return the k largest distinct elements in arr.
*/

//Java code:
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int[] maximum(int[] arr, int k) {
        Arrays.sort(arr);
        int[] res = new int[k];
        int j = 0;
        for(int i = arr.length - 1; i >= arr.length - k;