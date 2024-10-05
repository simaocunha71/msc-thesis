    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(i % 3 == 0){
            sum += lst[i] * lst[i] * lst[i];
        }else if(i % 4 == 0){
            sum += lst[i] * lst[i];
        }else{
            sum += lst[i];
        }
    }
    return sum;
}
*/

#include <iostream>
#include <vector>

using namespace std;

int sum_squares(vector<int> lst){
    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(i % 3 == 0){
            sum += lst[i] * lst[i] * lst[i];
        }else if(i % 4 == 0){
            sum += lst[i] * lst[i];
        }else{
            sum += lst[i];
        }
    }
    return sum;
}

int main()
{
    vector<int> lst = {1,2,3};
    cout << sum_squares(lst) << endl;
    lst = {};
    cout << sum_squares(lst) << endl;
    lst = {-1,-5,2,-1,-5};
    cout << sum_squares(lst) << endl;
    return 0;
}

// C++ program to solve the problem.
// 