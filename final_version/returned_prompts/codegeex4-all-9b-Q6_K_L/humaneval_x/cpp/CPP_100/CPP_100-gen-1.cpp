#include<stdio.h>
#include<vector>
using namespace std;
vector<int> make_a_pile(int n){
    vector<int> pile;
    pile.push_back(n);
    while(n){
        n = n%2 ? n+2 : n+1;
        pile.push_back(n);
    }
    return pile;
}

