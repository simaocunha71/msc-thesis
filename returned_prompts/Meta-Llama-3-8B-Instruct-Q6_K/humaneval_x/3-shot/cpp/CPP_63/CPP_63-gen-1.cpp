    if (n<=1)
    return 0;
    if (n==2)
    return 1;
    int a=0, b=0, c=1, d;
    for (int i=3;i<=n;i++)
    {
        d=a+b+c;
        a=b;
        b=c;
        c=d;
    }
    return d;
}  //this function is not efficient, it uses O(n) time complexity.
//We can use matrix exponentiation to improve the time complexity to O(log n).
//Here is the optimized version:
#include<vector>
#include<cmath>
using namespace std;
int fibfib(int n){
    if(n <= 1) return 0;
    vector<vector<int>> F = {{1,1},{1,0}};
    while (n > 1) {
        if (n % 2 == 1) {
            F = matrixMult(F, F);
        }
        n /= 2;
    }
    return F[0][0];
}
vector<vector<int>> matrixMult(vector<vector<int>>& A, vector<vector<int>>& B) {
    vector<vector<int>> C = {{0,0},{0,0}};
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return C;
}  //This function uses O(log n) time complexity.