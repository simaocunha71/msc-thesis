    int count = 0;
    int n = arr.size();
    for(int i = 0; i <= n/2; i++) {
        if(arr[i] != arr[n-i-1]) {
            count++;
        }
    }
    return count;
}

int main(){
    vector<int> arr = {1, 2, 3, 2, 1};
    printf("%d", smallest_change(arr));
    return 0;
}
*/

//C++/C++_Code/Palindrome_Vector_Min_Changes.cpp
#include<stdio.h>
#include<vector>
using namespace std;
int smallest_change(vector<int> arr){
    int count = 0;
    int n = arr.size();
    for(int i = 0; i <= n/2; i++) {
        if(arr[i] != arr[n-i-1]) {
            count++;
        }
    }
    return count;
}

int main(){
    vector<int> arr = {1, 2, 3, 2, 1};
    printf("%d", smallest_change(arr));
    return 0;
}

//C++/C++_Code/Palindrome_Vector_Min_Changes_Test.cpp
#include<vector>
#include<assert.h>
#include "Palindrome_Vector_Min_Changes.cpp"
using namespace std;

int main(){
    assert(smallest_change(vector<int>{1,2,3,5,4,7,9,6}) == 4);
    assert(smallest_change(vector<int>{1, 2, 3, 4, 3, 2, 2}) == 1);
    assert(smallest_change(vector<int>{1, 2, 3, 2, 1}) == 0);
    assert(smallest_change(vector<int>{1}) == 0);
    assert(smallest_change(vector<int>{1, 2, 2, 1}) == 0);
   