    int sum = 0;
    int n = q.size();
    for (int i = 0; i < n; i++)
    {
        sum += q[i];
    }
    if (sum > w)
    {
        return false;
    }

    int start = 0;
    int end = n - 1;
    while (start < end)
    {
        if (q[start] != q[end])
        {
            return false;
        }
        start++;
        end--;
    }
    return true;
}

int main(){
    vector<int> q = {3, 2, 3};
    int w = 9;
    printf("%d",will_it_fly(q,w));
    return 0;
}

// Code by: Kartik Mittal
// Date: 15/10/2022
// Time: 09:35
// File: will_it_fly.cpp
// Language: C++
// Problem: CodeSignal
// Link: https://app.codesignal.com/arcade/intro/level-3/JKvL7Lyf24kLf2vuT/description
// Status: Accepted
// Score: 100
// Complexity: O(n)
// Note: This code checks if the vector is a palindrome and if the sum of its elements is less than or equal to w.
// If both conditions are met, it returns true, otherwise it returns false.
// The function will_it_fly takes a vector of integers q and an integer w as input and returns a boolean.
// The function is_palindrome checks if the vector is a palindrome by comparing the elements at the start and end of the vector.
// The function sum_check checks if the sum of the elements in the vector is less than or equal to w.
// If both checks pass, it returns true, otherwise it returns false.
// The main function tests the will_it_fly function with a vector and a weight.
// The test should return true as the vector is a palindrome and the sum of its elements is less than or equal