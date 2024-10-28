    int i = 0;
    while(i < arr.size()) {
        if (arr[i] > arr[i - 1]) {
            break;
        }
        i++;
    }
    if (i == arr.size()) {
        return -1;
    }
    int j = i + 1;
    while (j < arr.size()) {
        if (arr[i] > arr[j]) {
            return -1;
        }
        j++;
    }
    return i;
}

int main(){
    vector<int> arr;
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(4);
    arr.push_back(3);
    arr.push_back(5);
    printf("%d", can_arrange(arr));
}










*/
#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<climits>
#include<cfloat>
#include<map>
#include<set>
#include<sstream>
#include<cstdio>
#include<stack>
#include<queue>
#include<cstring>
#include<list>
#include<numeric>
#include<functional>
#include<cassert>
#include<iomanip>

using namespace std;

int main()
{
    vector<int> arr;
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(4);
    arr.push_back(3);
    arr.push_back(5);
    cout << can_arrange(arr) << endl;

    return 0;
}


int can_arrange(vector<int> arr)
{
    int i = 0;
    while(i < arr.size()) {
        if (arr[i] > arr[i - 1]) {
            break;
        }
        i++;
    }
    if (i == arr.size()) {
       