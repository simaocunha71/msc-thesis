    int sum = array[0] + array[array.size()-1];
    if (sum % 2 == 0) {
        sort(array.begin(), array.end(), greater<int>());
    } else {
        sort(array.begin(), array.end());
    }
    return array;
}  // return a copy of the given vector after sorting
// if the sum( first index value, last index value) is odd, sort the given vector in ascending order
// or sort it in descending order if the sum( first index value, last index value) is even.  //  // don't change the given vector.  //  // Examples:
// * sort_vector({}) => {}
// * sort_vector({5}) => {5}
// * sort_vector({2, 4, 3, 0, 1, 5}) => {0, 1, 2, 3, 4, 5}
// * sort_vector({2, 4, 3, 0, 1, 5, 6}) => {6, 5, 4, 3, 2, 1, 0}  //  // Note:
// * don't change the given vector.  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //