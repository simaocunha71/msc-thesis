#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
vector<int> tri(int n){
    if (n == 0) return {0};
    if (n == 1) return {0,1};
    if (n == 2) return {0,1,1};
    vector<int> res(n+1);
    res[0] = 0;
    res[1] = 1;
    res[2] = 1;
    for (int i = 3; i <= n; i++){
        if (i % 2 == 0){
            res[i] = res[i-1] + res[i-2] + res[i-3] + 1;
        }
        else{
            res[i] = res[i-1] + res[i-2] + res[i-3];
        }
    }
    return res;
}

B:
#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
vector<int> tri(int n){
    if (n == 0) return {0};
    if (n == 1) return {0,1};
    if (n == 2) return {0,1,1};
    vector<int> res(n+1);
    res[0] = 0;
    res[1] = 1;
    res[2] = 1;
    for (int i = 3; i <= n; i++){
        res[i] = res[i-1] + res[i-2] + res[i-3] + 1;
    }
    return res;
}

C:
#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
vector<int> tri(int n){
    if (n == 0) return {0};
    if (n == 1) return {0,1};
    if (n == 2) return {0,1,1};
    vector<int> res(n+1);
    res[0] = 0;
    res[1] = 1;
    res[2] = 1;
    for (int i = 3; i <= n; i++){
        if (i % 2 == 0){
            res[i] = res[i-1] + res[i-2] + res[i-3];
        }
        else{
            res[i] = res[i-1] + res[i