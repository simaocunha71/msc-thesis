    int balance = 0;
    for (int i = 0; i < operations.size(); i++) {
        balance += operations[i];
        if (balance < 0) {
            return true;
        }
    }
    return false;
}  //  end of function below_zero


C:
    int main() {
        vector<int> operations = {1, 2, 3};
        printf("%d\n", below_zero(operations)); // prints 0
        operations = {1, 2, -4, 5};
        printf("%d\n", below_zero(operations)); // prints 1

        return 0;
    }  // end of main function


D:
    int main() {
        vector<int> operations = {1, 2, 3};
        printf("%d\n", below_zero(operations)); // prints 0
        operations = {1, 2, -4, 5};
        printf("%d\n", below_zero(operations)); // prints 1

        return 0;
    }  // end of main function

E:
    int main() {
        vector<int> operations = {1, 2, 3};
        printf("%d\n", below_zero(operations)); // prints 0
        operations = {1, 2, -4, 5};
        printf("%d\n", below_zero(operations)); // prints 1

        return 0;
    }  // end of main function


F:
    int main() {
        vector<int> operations = {1, 2, 3};
        printf("%d\n", below_zero(operations)); // prints 0
        operations = {1, 2, -4, 5};
        printf("%d\n", below_zero(operations)); // prints 1

        return 0;
    }  // end of main function
G:
    int main() {
        vector<int> operations = {1, 2, 3};
        printf("%d\n", below_zero(operations)); // prints 0
        operations = {1, 2, -4, 5};
        printf("%d\n", below_zero(operations)); // prints 1

        return 0;
    }  // end of main function


H:
    int main() {
        vector<int> operations = {1, 2, 3};
        printf("%d\n", below_zero(operations)); // prints 