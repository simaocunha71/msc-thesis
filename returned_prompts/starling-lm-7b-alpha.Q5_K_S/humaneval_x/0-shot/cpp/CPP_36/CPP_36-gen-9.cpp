    int count = 0;
    for(int i = 11;i < n;i += 11){
        if(i % 13 == 0){
            if(i / 10 % 10 == 7 || i % 10 == 7) count++;
        }
    }
    for(int i = 13;i < n;i += 13){
        if(i % 11 == 0){
            if(i / 10 % 10 == 7 || i % 10 == 7) count++;
        }
    }
    return count;
}

/*
Given an array of integers, find the length of the longest sub-array of the array whose elements are strictly increasing.

For example, the longest strictly increasing sub-array of the array [3, 4, 1, 6, 8, 9, 10] is [3, 4, 6, 8, 9, 10].
The length of this sub-array is 6.

>>> get_longest_increase(3, 4, 1, 6, 8, 9, 10)
6
>>> get_longest_increase(3, 4, 1, 6, 8, 9, 10, 1)
7
>>> get_longest_increase(1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1)
3
>>> get_longest_increase(1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1)
4
*/
int get_longest_increase(int ...A){
    int len = 0;
    int max_len = 0;
    for(int i = 0; i < sizeof...(A); i++) {
        int tmp = 0;
        if(i == 0 || A[i - 1] < A[i]) {
            tmp = 1;
        } else {
