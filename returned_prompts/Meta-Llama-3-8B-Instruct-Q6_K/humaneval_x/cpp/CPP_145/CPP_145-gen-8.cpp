    // Sort the vector based on the sum of digits and the original index
    sort(nums.begin(), nums.end(), 
         [](int a, int b) {
             int sumA = 0, sumB = 0;
             for (int i = a; i != 0; i /= 10)
                 sumA += i % 10;
             for (int i = b; i != 0; i /= 10)
                 sumB += i % 10;
             if (sumA == sumB)
                 return a < b;  // If sum of digits is same, then sort based on original index
             return sumA < sumB; // If sum of digits is different, then sort based on sum of digits
         });
    return nums;
}

B:
    sort(nums.begin(), nums.end(), 
         [](int a, int b) {
             int sumA = 0, sumB = 0;
             for (int i = abs(a); i != 0; i /= 10)
                 sumA += i % 10;
             for (int i = abs(b); i != 0; i /= 10)
                 sumB += i % 10;
             if (sumA == sumB)
                 return a < b;  // If sum of digits is same, then sort based on original index
             return sumA < sumB; // If sum of digits is different, then sort based on sum of digits
         });
    return nums;
}
C:
    sort(nums.begin(), nums.end(), 
         [](int a, int b) {
             int sumA = 0, sumB = 0;
             for (int i = abs(a); i != 0; i /= 10)
                 sumA += i % 10;
             for (int i = abs(b); i != 0; i /= 10)
                 sumB += i % 10;
             return sumA < sumB;  // Sort based on sum of digits
         });
    return nums;
}

D:
    sort(nums.begin(), nums.end(), 
         [](int a, int b) {
             int sumA = 0, sumB = 0;
             for (int i = abs(a); i != 0; i /= 10)
                 sumA += i % 10;
             for (int i = abs(b); i != 0; i /= 10)
                