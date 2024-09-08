    // check if sum of first and last element is odd or even
    int sum = array[0] + array[array.size() - 1];
    if(sum % 2 == 0){ // if sum is even, sort in descending order
        sort(array.begin(), array.end(), greater<int>());
    }else{ // if sum is odd, sort in ascending order
        sort(array.begin(), array.end());
    }
    return array;
}

int main(){
    vector<int> array = {2, 4, 3, 0, 1, 5};
    array = sort_array(array);
    for(int i = 0; i < array.size(); i++){
        printf("%d ", array[i]);
    }
    printf("\n");
    return 0;
}

Output:
0 1 2 3 4 5 

In the above problem, we need to sort the given array in ascending order if the sum of the first and last element is odd, otherwise in descending order. We can do this by checking the sum and then sorting the array accordingly. We use the `std::sort` function from the `<algorithm>` library to sort the array. We also use the `greater<int>` function object to sort the array in descending order. If the sum is even, we use `greater<int>()` as the comparator, otherwise we use no comparator (which is the default, which is ascending order). The sorted array is then returned. 

In the main function, we test this function with a given array and print the result. The output is as expected. 

Note: This problem is a variation of the classic problem of sorting an array in ascending or descending order based on a condition. The condition here is the sum of the first and last element, which is a unique twist on the classic problem.