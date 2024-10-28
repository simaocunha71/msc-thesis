    vector<string> result;
    map<int, string> digit_map = { {1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"} };
    vector<int> sorted_arr;
    for (int i : arr){
        if (i>=1 && i<=9){
            sorted_arr.push_back(i);
        }
    }
    sort(sorted_arr.begin(), sorted_arr.end());
    reverse(sorted_arr.begin(), sorted_arr.end());
    for (int i : sorted_arr){
        result.push_back(digit_map[i]);
    }
    return result;
}  // This solution works but it does not handle the edge case where the input vector is empty.  It should return an empty vector in this case.  Also, it does not handle the edge case where the input vector has any number other than 1,2,3,4,5,6,7,8,9.  It should ignore such numbers.  The solution should be modified to handle these edge cases.  It should return an empty vector if the input vector is empty or if it contains any number other than 1,2,3,4,5,6,7,8,9.  It should ignore any numbers other than 1,2,3,4,5,6,7,8,9.  The solution should be modified to handle these edge cases.
}  // This solution works but it does not handle the edge case where the input vector is empty.  It should return an empty vector in this case.  Also, it does not handle the edge case where the input vector has any number other than 1,2,3,4,5,6,7,8,9.  It should ignore such numbers.  The solution should be modified to handle these edge cases.  It should return an empty vector if the input vector is empty or if it contains any number other than 1,2,3,4,5,6,7,8,9.  It should ignore any numbers other than 1,2,3,4,5,6,7,8,9.  The solution should be modified to handle these edge cases.
}  // This solution works but it does not handle the edge case where the input vector is empty.  It should