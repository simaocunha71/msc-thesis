    int balance = 0;
    for (int i=0; i<operations.size(); i++){
        balance += operations[i];
        if (balance < 0){
            return true;
        }
    }
    return false;
}
int main() {
    vector<int> deposit_withdrawal = {1, 2, 3};
    printf("%s\n", below_zero(deposit_withdrawal) ? "true" : "false");
    deposit_withdrawal = {1, 2, -4, 5};
    printf("%s\n", below_zero(deposit_withdrawal) ? "true" : "false");
    return 0;
}
*/


