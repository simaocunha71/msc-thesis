/*
You will be given an array of integers. Your task is to find the first positive integer
in the array. If there is no positive integer in the array, return -1.

Examples:
[1, 2, 3, 4, 5, 6]   // returns 1
[1, -2, 3, -4, 5, 6] // returns 1
[-1, -2, -3, -4, -5, -6] // returns -1
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int first_positive(int arr[], int size)
{
    for(int i = 0; i < size; i++)
    {
        if(arr[i] > 0)
            return arr[i];
    }
    return -1;
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6};
    int size = sizeof(arr) / sizeof(arr[0]);
    int result = first_positive(arr, size);
    printf("%d", result);
    return 0;
}

