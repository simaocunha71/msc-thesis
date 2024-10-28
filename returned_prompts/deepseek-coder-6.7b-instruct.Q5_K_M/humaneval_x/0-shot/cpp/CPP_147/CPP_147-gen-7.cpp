    vector<int> a(n);
    int count = 0;
    for(int i=1; i<=n; i++){
        a[i-1] = i*i - i + 1;
    }
    for(int i=0; i<n-2; i++){
        for(int j=i+1; j<n-1; j++){
            for(int k=j+1; k<n; k++){
                if((a[i] + a[j] + a[k]) % 3 == 0)
                    count++;
            }
        }
    }
    return count;
}

int main(){
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("%d", get_matrix_triples(n));
    return 0;
}

This code works by first creating a vector 'a' of length 'n' and filling it with the values of the formula i*i - i + 1 for each i in the range 1 to n. Then, it iterates over all possible triples of indices (i, j, k) in the vector and increments a counter if the sum of the elements at the indices i, j, and k is a multiple of 3. The function then returns the counter.
The time complexity of this code is O(n^3) because it performs a triple nested loop over the vector.
*/

#include <stdio.h>
#include <vector>
using namespace std;

int get_matrix_triples(int n) {
    vector<int> a(n);
    int count = 0;
    for (int i = 1; i <= n; i++) {
        a[i-1] = i*i - i + 1;
    }
    for (int i = 0; i < n-2; i++) {
        for (int j = i+1; j < n-1; j++) {
            for (int k = j+1; k < n; k++) {
                if ((a[i] + a[j] + a[k]) % 3 == 0)
                    count++