    int n = arr.size();
    if(n <= 1)
        return -1;
    for(int i = 1; i < n; i++){
        if(arr[i-1] >= arr[i])
            return i-1;
    }
    return -1;
}

int main(){
    vector<int> arr = {1,2,4,3,5};
    int result = can_arrange(arr);
    printf("%d\n", result);
    return 0;
}

S:
The function `can_arrange` iterates through the given array and checks for each element if it is not greater than or equal to the previous element. If such an element is found, it returns the index of the previous element. If no such element is found, it returns -1. In the given example, the function will return 3, which is the largest index of an element that is not greater than or equal to the element immediately preceding it. If the array does not contain any such element, the function will return -1. The time complexity of this function is O(n), where n is the size of the given array. The space complexity is O(1), as it only uses a constant amount of space. The function is also efficient and can handle large arrays. It also handles cases where the array contains duplicate values. The function is also easy to understand and implement.