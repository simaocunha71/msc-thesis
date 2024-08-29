/*
You are given an array a of length n. Find the number of triples (a{i}, a{j}, a{k}) of a where i < j < k, 
and a[i] + a[j] + a[k] is a multiple of 3.

Example :
    Input: a = {1, 2, 3, 4, 5}
    Output: 3
    Explanation: 
    The valid triples are (1, 2, 4), (1, 3, 5), (2, 3, 5).
*/
#include<stdio.h>
#include<vector>
using namespace std;
int get_matrix_triples(vector<int> a){
*/

#include<stdio.h>
#include<vector>
using namespace std;
int get_matrix_triples(int n){
vector<int> a;
for(int i=1;i<=n;i++){
    a.push_back(i*i-i+1);
}
int count=0;
for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
        for(int k=j+1;k<n;k++){
            if((a[i]+a[j]+a[k])%3==0){
                count++;
            }
        }
    }
}
return count;
}

int get_matrix_triples(vector<int> a){
int n=a.size();
int count=0;
for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
        for(int k=j+1;k<n;k++){
            if((a[i]+a[j]+a[k])%3==0){
                count++;
            }
        }
    }
}
return count;
}

int main(){
int n=5;
vector<int> a={1, 2, 3, 4, 5};

printf("%d\n",get_matrix_triples(n));
printf("%d\n",get_matrix_triples(a));
return 0;
}


###PATH:./Q-3.cpp
#include<stdio.h>
#include<vector>
using namespace std;
int get_matrix_triples(int n){
vector<int> a;
for(int i=1;i<=n;i++){
    a.push_back(i*i-i+1);
}
int count=0;
for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
        for(int k=j+1;k<n;k++){
            if((a[i]+a[j]+a[k])%3==0){
                count++;
            }
        }
    }
}
return count;
}

int