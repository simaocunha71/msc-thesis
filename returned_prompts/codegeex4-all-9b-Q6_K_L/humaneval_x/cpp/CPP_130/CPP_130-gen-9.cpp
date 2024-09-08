#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){
    vector<int> res;
    if (n == 0) return res;
    res.push_back(3);
    for (int i = 1; i <= n; i++){
        int tmp = 1 + i / 2;
        if (i % 2 == 1) tmp += res[i - 1];
        res.push_back(tmp);
    }
    return res;
}

B:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){
    vector<int> res;
    if (n == 0) return res;
    res.push_back(3);
    for (int i = 1; i <= n; i++){
        int tmp = 1 + i / 2;
        if (i % 2 == 0) tmp += res[i - 1];
        res.push_back(tmp);
    }
    return res;
}

C:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){
    vector<int> res;
    if (n == 0) return res;
    res.push_back(3);
    for (int i = 1; i <= n; i++){
        int tmp = 1 + i / 2;
        if (i % 2 == 0) tmp += res[i - 1];
        if (i % 2 == 1) tmp += res[i - 1];
        res.push_back(tmp);
    }
    return res;
}

D:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){
    vector<int> res;
    if (n == 0) return res;
    res.push_back(3);
    for (int i = 1; i <= n; i++){
        int tmp = 1 + i / 2;
        if (i % 2 == 1) tmp += res[i - 1];
        if (i % 2 == 0) tmp += res[i - 1];
        res.push_back(tmp);
    }
    return res;
}

E:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){
    vector<int> res;
    if (n == 0) return res;
    res.push_back(3);
    for (int i = 1; i <= n; i++){
        int tmp = 