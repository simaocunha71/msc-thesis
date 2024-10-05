    int i = 2;
    while (n % i != 0) {
        i++;
    }
    return i - 1;
}



/*
Given a number, find all the primes smaller than it.
>>> smallest_primes([1, 3, 5, 7, 8])
[2, 3, 5]
*/
int smallest_primes(int arr[], int n) {
    for (int i = 2; i < n; i++) {
        int j = 2;
        while (j * j <= i) {
            if (i % j == 0) {
                break;
            }
            j++;
        }
        if (j * j > i) {
            arr[i] = i;
        }
    }
    return arr;
}



/*
Given an array of integers, find the smallest number that appears more than n/2 times.
If there are multiple such numbers, return the smallest one.

>>> smallest_majority_element([3, 2, 3, 2, 3, 2, 3])
3
>>> smallest_majority_element([3, 2, 3, 2])
2
>>> smallest_majority_element([9, 8, 7, 6, 5, 4, 3, 2, 1])
1

Note: This function may not work if the input array has duplicate elements.

*/
int smallest_majority_element(int arr[], int n) {
    int i = 0;
    int count = 1;
    int min_index = i;
    while (i < n) {
        if (arr[i] == arr[min_index]) {
            count++;
        } else {
            count--;
        }
        if (count == 0) {
            min_index = i;
            count = 1;
        }
        i++;
    }
    return arr[min_index];
}


/*
Given a number, find all the prime numbers smaller than it.
>>> smallest_primes_smaller_than(15)