    int balance = 0;
    for(int i=0; i<operations.size(); i++){
        balance += operations[i];
        if(balance < 0){
            return true;
        }
    }
    return false;
}

int main(){
    vector<int> operations1 = {1, 2, 3};
    vector<int> operations2 = {1, 2, -4, 5};
    printf("%d\n", below_zero(operations1));
    printf("%d\n", below_zero(operations2));
    return 0;
}

*/

int main() {
    printf("Hello, World!\n");
    return 0;
}

//cpp/exercises/15_bank_account/main.cpp
#include <iostream>
#include <vector>
using namespace std;

bool below_zero(vector<int> operations) {
    int balance = 0;
    for(int i = 0; i < operations.size(); i++) {
        balance += operations[i];
        if(balance < 0) {
            return true;
        }
    }
    return false;
}

int main() {
    vector<int> operations1 = {1, 2, 3};
    vector<int> operations2 = {1, 2, -4, 5};
    cout << boolalpha << below_zero(operations1) << endl;
    cout << boolalpha << below_zero(operations2) << endl;
    return 0;
}

//cpp/exercises/2_print_number/main.cpp
#include <iostream>

int main() {
    int number = 42;
    std::cout << number << std::endl;
    return 0;
}

//cpp/exercises/3_variables/main.cpp
#include <iostream>

int main() {
    int number = 42;
    double decimal = 3.14;
    char letter = 'A';
    std::cout << number << std::endl;
    std::c