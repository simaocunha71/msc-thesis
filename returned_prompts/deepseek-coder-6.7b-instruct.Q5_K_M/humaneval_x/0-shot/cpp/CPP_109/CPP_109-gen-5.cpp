    int n = arr.size();

    if(n == 0)
        return true;

    int count = 0;
    for(int i = 0; i < n - 1; i++){
        if(arr[i] > arr[i + 1])
            count++;
    }

    if(arr[n - 1] > arr[0])
        count++;

    if(count > 1)
        return false;

    return true;
}

int main(){
    vector<int> arr = {3, 4, 5, 1, 2};
    if(move_one_ball(arr))
        printf("true\n");
    else
        printf("false\n");

    return 0;
}

*/

// This code is a function to check if it is possible to sort the array by performing at most one right shift operation.
// It uses a simple for loop to traverse the array and count the number of times the current element is greater than the next one.
// If there are more than one such occurrences, it means we can't sort the array by performing at most one right shift operation, so it returns false.
// If the count is less than or equal to one, it means we can sort the array by performing at most one right shift operation, so it returns true.
// If the array is empty, it