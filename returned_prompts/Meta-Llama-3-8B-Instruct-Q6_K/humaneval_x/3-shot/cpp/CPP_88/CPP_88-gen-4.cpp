    int sum = array[0] + array[array.size()-1];
    if (sum % 2 == 0) {
        sort(array.begin(), array.end(), greater<int>());
    } else {
        sort(array.begin(), array.end());
    }
    return array;
}
// Note: This solution modifies the input array. If you don't want to modify the array, 
// you can return a new vector instead of returning the input array. 
// You can achieve this by using the following code: 
// return vector<int>(array.begin(), array.end()); 
// This creates a copy of the input array. 
// So, the final code would be: 
// vector<int> sort_array(vector<int> array) { 
//     int sum = array[0] + array[array.size()-1]; 
//     if (sum % 2 == 0) { 
//         sort(array.begin(), array.end(), greater<int>()); 
//     } else { 
//         sort(array.begin(), array.end()); 
//     } 
//     return vector<int>(array.begin(), array.end()); 
// } 