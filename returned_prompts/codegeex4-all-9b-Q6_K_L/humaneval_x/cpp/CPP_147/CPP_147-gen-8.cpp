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

*/
int count = 0;
vector<int> a(n);
for(int i=0; i<n; i++){
    a[i] = i*i - i + 1;
}
for(int i=0; i<n; i++){
    for(int j=i+1; j<n; j++){
        for(int k=j+1; k<n; k++){
            if((a[i]+a[j]+a[k])%3==0){
                count++;
            }
        }
    }
}
return count;
}
int main(){
int n;
scanf("%d", &n);
int result = get_matrix_triples(n);
printf("%d", result);
return 0;
}

B:
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

*/
int count = 0;
vector<int> a(n);
for(int i=0; i<n; i++){
    a[i] = i*i - i + 1;
}
for