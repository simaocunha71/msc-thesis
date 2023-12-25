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
    vector<int> a(n);
    for( int i=0 ; i<n ; i++ ){a[i] = i*i;}
    
    int n = 5, triples = 0;
    for( int i = 1 , j = 2, k = 3 ; 
            (j < k) && ((a[i]+a[j]+a[k]) % 3 == 0);
        ) {
        //find all the triples of the form a[x] + a[y] + a[z], where x < y < z
        if((triples+1)%3 != 0){
            //if any triple is not valid, reset it to zero
            triples = 0;
        }
        if(!( (a[i]+a[j]+a[k]) % 3 == 0)){
            // if the three values form a triple which are 1)valid and 2)not part of any other triples
            triples++;
        }   
        printf("\n %d ", triples);    
    for( int l = i,r=j+1;l<r ;l++)
        {printf(" %d\n",a[l]);}     
        if((triples % 3) != 0){  //if the modulo of triples