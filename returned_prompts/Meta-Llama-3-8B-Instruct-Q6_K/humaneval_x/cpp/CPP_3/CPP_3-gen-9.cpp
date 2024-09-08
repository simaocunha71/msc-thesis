    int balance = 0;
    for(int operation: operations){
        balance += operation;
        if(balance < 0){
            return true;
        }
    }
    return false;
} // end of function below_zero

int main(){
    vector<int> operations = {1, 2, 3};
    bool result = below_zero(operations);
    printf("%d\n", result);
    return 0;
}

Output:
false
Explanation: In this problem, we need to check if the balance of the account goes below zero. We are given a vector of operations which are either deposits or withdrawals. We initialize the balance to zero and then iterate over the operations. For each operation, we add it to the balance. If the balance ever becomes negative, we return true, indicating that the balance did go below zero. If we finish iterating over all operations without the balance ever going below zero, we return false. In this example, the operations are {1, 2, 3}, so the balance will always be positive and we return false. If we change the operations to {1, 2, -4, 5}, then the balance will go below zero when we subtract 4, so we return true.