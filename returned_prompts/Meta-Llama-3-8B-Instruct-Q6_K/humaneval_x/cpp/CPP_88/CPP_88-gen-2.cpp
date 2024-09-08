    if(array.empty())
        return array;
    int sum = array[0] + array[array.size() - 1];
    if(sum % 2 == 0)
        sort(array.begin(), array.end(), greater<int>());
    else
        sort(array.begin(), array.end());
    return array;
}
int main() {
    vector<int> array = {2, 4, 3, 0, 1, 5};
    array = sort_array(array);
    for(int i = 0; i < array.size(); i++)
        printf("%d ", array[i]);
    printf("\n");
    return 0;
}

O/P:
0 1 2 3 4 5

Explanation:
This program defines a function sort_array() that takes a vector of integers as input. It calculates the sum of the first and last elements of the vector. If the sum is even, it sorts the vector in descending order. If the sum is odd, it sorts the vector in ascending order. It returns the sorted vector.

In the main() function, we create a vector array and pass it to the sort_array() function. We then print the sorted array.

In this example, the sum of the first and last elements of the array is 2 + 5 = 7, which is odd. So, the array is sorted in ascending order. The output is {0, 1, 2, 3, 4, 5}. If the sum were even, the array would be sorted in descending order.