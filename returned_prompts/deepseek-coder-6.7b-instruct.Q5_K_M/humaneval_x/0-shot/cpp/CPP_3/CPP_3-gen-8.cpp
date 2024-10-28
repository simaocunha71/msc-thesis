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
    vector<int> deposit_withdrawal = {1, 2, -4, 5};
    if(below_zero(deposit_withdrawal)){
        printf("Account balance went below zero at some point\n");
    }
    else{
        printf("Account balance stayed at zero or above zero\n");
    }
    return 0;
}

Note:
This solution assumes that the vector passed to the function contains only deposit and withdrawal operations (positive and negative numbers respectively). If there are any other types of operations, this solution may not work correctly.
Also, it assumes that the balance does not exceed the maximum value that can be represented by an int in C++. If that's not the case, this solution will not work.
*/

