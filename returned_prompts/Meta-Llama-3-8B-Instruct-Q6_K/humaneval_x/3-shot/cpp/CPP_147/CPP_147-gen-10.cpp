    vector<int> a(n+1);
    int count = 0;
    for(int i=1; i<=n; i++) {
        a[i] = i * i - i + 1;
    }
    for(int i=1; i<n; i++) {
        for(int j=i+1; j<n; j++) {
            for(int k=j+1; k<=n; k++) {
                if((a[i] + a[j] + a[k]) % 3 == 0) {
                    count++;
                }
            }
        }
    }
    return count;
}  // This function returns the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
// and a[i] + a[j] + a[k] is a multiple of 3.  // The input parameter 'n' is a positive integer. 
// The function returns an integer. 
// The function calculates the sum of each triple and checks if it is divisible by 3. 
// If it is, it increments the count. 
// Finally, it returns the count. 
// The time complexity of this function is O(n^3) and the space complexity is O(n). 
// The space complexity is O(n) because we are storing 'n' elements in the vector 'a'. 
// The time complexity is O(n^3) because we are using three nested for loops. 
// The outer loop runs 'n' times, the middle loop also runs 'n' times, 
// and the inner loop runs 'n' times. 
// So, the total number of operations is n * n * n. 
// The function can be optimized by reducing the number of operations. 
// For example, we can stop the inner loop as soon as we find a triple that satisfies the condition. 
// We can also reduce the number of operations by using a more efficient algorithm. 
// The function can be further optimized by using a more efficient data structure, 
// such as a hash table, to store the values of 'a'. 
// This would allow us to reduce the time complexity to O(n^2). 
// However, the function is currently implemented as O(n^3) because it is a simple and easy to understand solution. 
// The function can also be optimized by using a more efficient algorithm, 
// such as a dynamic programming approach. 
// This would allow us to reduce the