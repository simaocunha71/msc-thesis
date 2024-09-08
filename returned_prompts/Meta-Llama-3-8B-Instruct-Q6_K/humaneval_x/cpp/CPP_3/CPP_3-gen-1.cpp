    int balance = 0;
    for(int i = 0; i < operations.size(); i++){
        balance += operations[i];
        if(balance < 0){
            return true;
        }
    }
    return false;
} // close function below_zero

int main() {
    vector<int> operations = {1, 2, 3}; // example of deposit and withdrawal operations
    printf("%d\n", below_zero(operations)); // print result
    return 0;
} // close main

B:
    vector<int> operations = {1, 2, -4, 5}; // example of deposit and withdrawal operations
    printf("%d\n", below_zero(operations)); // print result
    return 0;
} // close main

