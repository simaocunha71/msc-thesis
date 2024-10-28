    int n = arr.size();
    int changes = 0;
    for(int i = 0; i < n / 2; i++){
        if(arr[i] != arr[n - i - 1]){
            changes++;
        }
    }
    return changes;
}

int main() {
    vector<int> arr = {1, 2, 3, 5, 4, 7, 9, 6};
    printf("%d\n", smallest_change(arr));
    return 0;
}

*/

/*
I:
{1, 2, 3, 5, 4, 7, 9, 6}
O:
4

I:
{1, 2, 3, 4, 3, 2, 2}
O:
1

I:
{1, 2, 3, 2, 1}
O:
0
*/

/*
T:
The function smallest_change takes a vector of integers as input. It iterates over the first half of the vector,
comparing each element with the corresponding element from the end. If the elements are not equal, it increments
the count of changes. Finally, it returns the count of changes, which represents the minimum number of elements
that need to be changed to make the vector palindromic.
*/

/*
C:
The code defines a function smallest_change that takes a vector of integers as input. The function iterates over the
first half of the vector, comparing each element with the corresponding element from the end. If the elements are
not equal, it increments the count of changes. Finally, it returns the count of changes. The main function tests
the function with a few examples and prints the result.
*/

/*
E:
The expected output for the given inputs is as follows:

Input: {1, 2, 3, 5, 4, 7, 9, 6}
Output: 4

Input: {1, 2, 3, 4, 3, 2, 2}
Output: 1

Input: {1, 2, 3, 2, 1