    int balance = 0;
    for (int i = 0; i < operations.size(); i++) {
        balance += operations[i];
        if (balance < 0) {
            return true;
        }
    }
    return false;
}
int main() {
    vector<int> operations = {1, 2, 3};
    bool result = below_zero(operations);
    printf("%d\n", result);
    return 0;
}

