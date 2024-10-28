    int balance=0;
    for(int i=0; i<operations.size(); i++){
        balance += operations[i];
        if(balance<0){
            return true;
        }
    }
    return false;
}

int main(){
    vector<int> test1 = {1, 2, 3};
    vector<int> test2 = {1, 2, -4, 5};
    printf("%d\n", below_zero(test1));
    printf("%d\n", below_zero(test2));
    return 0;
}
*/

