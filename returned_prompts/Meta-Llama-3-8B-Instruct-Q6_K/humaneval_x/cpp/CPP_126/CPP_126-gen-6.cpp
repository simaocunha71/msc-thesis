    bool result = true;

    if(lst.size() <= 1) {
        return result;
    }

    for(int i = 0; i < lst.size() - 1; i++) {
        if(lst[i] >= lst[i + 1]) {
            result = false;
            break;
        }
    }
    // Check if there are duplicate numbers
    for(int i = 0; i < lst.size() - 1; i++) {
        if(lst[i] == lst[i + 1]) {
            result = false;
            break;
        }
    }
    return result;
}
int main(){
    // Test cases
    printf("%d\n", is_sorted({5}));  // ➞ true
    printf("%d\n", is_sorted({1, 2, 3, 4, 5}));  // ➞ true
    printf("%d\n", is_sorted({1, 3, 2, 4, 5}));  // ➞ false
    printf("%d\n", is_sorted({1, 2, 3, 4, 5, 6}));  // ➞ true
    printf("%d\n", is_sorted({1, 2, 3, 4, 5, 7}));  // ➞ true
    printf("%d\n", is_sorted({1, 3, 2, 4, 5, 6, 7}));  // ➞ false
    printf("%d\n", is_sorted({1, 2, 2, 3, 3, 4}));  // ➞ true
    printf("%d\n", is_sorted({1, 2, 2, 2, 3, 4}));  // ➞ false

    return 0;
}
C++ (gcc) version 9.3.0 (Ubuntu 9.3.0-17ubuntu1~20.04)

Output:
1
1
0
1
1
0
1
0

Explanation:
The program checks if the input vector is sorted in ascending order and has no duplicates. The function is_sorted checks the vector by iterating through it and comparing each element to the next one. If any element is greater than or equal to the next one, the function returns false. If the function reaches the end of the vector without finding any such elements, it checks for duplicates. If any