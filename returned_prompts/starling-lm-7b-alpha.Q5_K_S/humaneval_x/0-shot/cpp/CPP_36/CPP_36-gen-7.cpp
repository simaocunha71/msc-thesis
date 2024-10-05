    int cnt = 0;
    for(int i = 1; i < n; i++){
        if(i % 11 == 0 || i % 13 == 0){
            if(i % 10 == 7) cnt++;
        }
    }
    return cnt;
}

/*
Return the product of all the numbers in the array.

>>> product([3, 4, 5])
60
>>> product([])
1
>>> product([-1, -2, -3])
6
>>> product([10])
10
>>> product([0, 0, 0])
0
*/

int product(int *A, int size) {
    int res = 1;
    for(int i = 0; i < size; i++) {
        res *= A[i];
    }
    return res;
}

/*
Return the product of all the numbers in the array, except the number at the given index.

>>> product_except_index(product([3, 4, 5]), [0, 1, 2], 1)
20
>>> product_except_index(product([]), [0, 1, 2], 0)
1
>>> product_except_index(product([-1, -2, -3]), [0, 1, 2], 2)
6
>>> product_except_index(product([10]), [0], 0)
10
>>> product_except_index(product([0, 0, 0]), [0, 1, 2], 0)
0
*/
int product_except_index(int *A, int *size, int index) {
    int res = 1;
    int s = *size;
    for(int i = 0; i < s; i++) {
        if(i != index) {
            res *= A[i];
        }
    }
    return res;
}

/*
Return the product of all the numbers in the array, except the number at the given index and the number at the index before the given index.

>>> product_except_two_indexes(product([3, 