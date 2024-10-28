    int n = arr.size();
    int max_idx = -1;
    for(int i=n-1; i>0; i--){
        if(arr[i] < arr[i-1]){
            max_idx = i;
            break;
        }
    }
    return max_idx;
}

int main(){
    vector<int> arr = {1, 2, 4, 3, 5};
    printf("%d\n", can_arrange(arr));
    return 0;
}

Ans:
The function can_arrange searches from the end of the array to find the first element which is less than the previous one. If such an element is found, the index of that element is returned. If no such element is found, -1 is returned.

In the example where arr = {1, 2, 4, 3, 5}, the function returns 3 because the element at index 3 (4) is less than the previous element (3), but no such element exists in the elements before index 3. Hence, -1 is returned.
*/

// @lc code=end

//Leetcode Problem 1656

/*
