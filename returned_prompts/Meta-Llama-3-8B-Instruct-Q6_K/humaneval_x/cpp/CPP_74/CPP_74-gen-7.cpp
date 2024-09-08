    vector<string> result;
    size_t sum1 = 0, sum2 = 0;
    for(auto s : lst1) sum1 += s.length();
    for(auto s : lst2) sum2 += s.length();

    if(sum1 < sum2) return lst1;
    else if(sum1 > sum2) return lst2;
    else return lst1;
}

// Test the function
int main() {
    vector<string> lst1 = {"hi", "admin"};
    vector<string> lst2 = {"hI", "Hi"};
    vector<string> result = total_match(lst1, lst2);
    for(auto s : result) printf("%s\n", s.c_str());
    return 0;
}  // Output: hI Hi
```

In this code, we are iterating over each string in the given vectors, and summing up the length of each string. We then compare the two sums. If the sum of the first vector is less than the sum of the second vector, we return the first vector. If the sum of the first vector is greater than the sum of the second vector, we return the second vector. If the sums are equal, we return the first vector. This way, we are effectively returning the vector with the total number of characters in all strings less than the other vector. If the sums are equal, we return the first vector as per the problem statement.