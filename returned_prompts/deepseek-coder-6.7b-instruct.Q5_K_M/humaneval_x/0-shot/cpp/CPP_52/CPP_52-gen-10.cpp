    for (int i=0; i<l.size(); i++){
        if (l[i] >= t){
            return false;
        }
    }
    return true;
}

int main(){
    vector<int> v1 = {1, 2, 4, 10};
    vector<int> v2 = {1, 20, 4, 10};
    printf("%d\n", below_threshold(v1, 100));
    printf("%d\n", below_threshold(v2, 5));
    return 0;
}
*/


A: Your function should return false if at least one number is not below the threshold and return true otherwise. So, you need to change return false; to return true; after the first number that is not below the threshold.
Also, the function printf() in C++ is used to print to the console. It expects int arguments, but you are providing bool ones. So, you need to change %d to %d.
Here's the correct code:
#include<iostream>
#include<vector>
using namespace std;

bool below_threshold(vector<int>l, int t){
    for (int i=0; i<l.size(); i++){
        if (l[i] >= t){
            return false;
        }
    }
    return true;
}

int main(){
    vector<int> v1 = {1, 2, 4, 10};
    vector<int> v2 = {1, 20, 4, 10};
    cout<< below_threshold(v1, 100)<<endl;
    cout<< below_threshold(v2, 5)<<endl;
    return 0;
}

Now, the program will print 1 for false and 0 for true.

A: Your program is almost correct. The only thing you should change is to return true when no elements in the vector are above the threshold. At the moment, you return false as soon as you find an element that is above the threshold.
Here is the corrected code:
#include <iostream>
#