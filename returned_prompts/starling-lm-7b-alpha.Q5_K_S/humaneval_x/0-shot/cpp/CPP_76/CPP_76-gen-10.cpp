int main() {
    int x, n;
    scanf("%d%d", &x, &n);
    bool simple_power = false;
    for (int i = 0; i <= 10; i++) {
        if (pow(n, i) == x) {
            simple_power = true;
            break;
        }
    }
    if (simple_power) {
        printf("true\n");
    } else {
        printf("false\n");
    }
    return 0;
}




/*
#include<bits/stdc++.h>
using namespace std;

bool is_simple_power(int x,int n){
    if (x==0||x==1) {
        return true;
    }
    if (n==0||n==1) {
        return false;
    }
    if (x<n) {
        return false;
    }
    if (x%n==0) {
        int p = log10(n);
        int q = log10(x);
        if (q==p) {
            return true;
       