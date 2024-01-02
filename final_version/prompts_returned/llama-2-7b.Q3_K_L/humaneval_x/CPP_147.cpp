/*
You are given a positive integer n. You have to create an integer vector a of length n.
    For each i (1 ≤ i ≤ n), the value of a{i} = i * i - i + 1.
    Return the number of triples (a{i}, a{j}, a{k}) of a where i < j < k, 
and a[i] + a[j] + a[k] is a multiple of 3.

Example :
    Input: n = 5
    Output: 1
    Explanation: 
    a = {1, 3, 7, 13, 21}
    The only valid triple is (1, 7, 13).
*/
#include<stdio.h>
#include<vector>
using namespace std;
int get_matrix_triples(int n){
    vector <int> a[n];
    int total =0;
    for(int i=1;i<=n;++i) {
        a[i][0] = i*i - i+1;
    }
    for(int i=1,j=2; j<n; ++i,++j){
        if((a[i-1][j]+a[i-1][j-1]+a[i-1][j-1])%3 == 0 && (a[i-1][j+1]+a[i-1][j]+a[i-1][j+1])%3==0)
            total++;
    }
    return total;
}
int main(){
    int n = get_matrix_triples(5);
    printf("%d",n);
    return 0;
}