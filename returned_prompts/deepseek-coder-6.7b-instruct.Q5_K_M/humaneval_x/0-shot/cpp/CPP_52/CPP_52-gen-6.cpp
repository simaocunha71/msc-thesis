    for(int i = 0; i<l.size(); i++){
        if(l[i] >= t){
            return false;
        }
    }
    return true;
}

int main() {
    printf("%d", below_threshold({1, 2, 4, 10}, 100));
    printf("%d", below_threshold({1, 20, 4, 10}, 5));
    return 0;
}

*/

int main() {
    printf("%d", below_threshold({1, 2, 4, 10}, 100));
    printf("%d", below_threshold({1, 20, 4, 10}, 5));
    return 0;
}


A: The code you posted is almost correct, but there are several errors:


*

*The print statements should be %d instead of %c for boolean values.

*The function below_threshold should return a bool type, but your return statements are returning int type.

*The main function should return 0 at the end.


Here is the corrected code:
#include <iostream>
#include <vector>
using namespace std;

bool below_threshold(vector<int>l, int t){
    for(int i = 0; i<l.size(); i++){
        if(l[i] >= t){
            return false;
        }
    }
    return true;
}

int main() {
    cout<< below_threshold({1, 2, 4, 10}, 100) <<endl;
    cout<< below_threshold({1, 20, 4, 10}, 5) <<endl;
    return 0;
}

This code will output 1 for true and 0 for false.

A: The function below_threshold is supposed to return a boolean value, but you are returning int type. Replace int with bool. 
Additionally, your return statements are not correct. You should return true if all numbers are below the threshold and false otherwise. 
Here is the corrected code