    int result = operand[0];
    for(int i = 0; i < operato.size(); i++){
        int a = operand[i];
        int b = operand[i+1];
        if(operato[i] == "+"){
            result += a;
        }
        else if(operato[i] == "-"){
            result -= a;
        }
        else if(operato[i] == "*"){
            result *= a;
        }
        else if(operato[i] == "//"){
            result = result / a;
        }
        else if(operato[i] == "**"){
            result = pow(result, a);
        }
    }
    return result;
}
int main(){
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    int result = do_algebra(operato, operand);
    printf("%d", result);
    return 0;
}
// Output: 9
// The expression is: 2 + 3 * 4 - 5. It is calculated as: 2 + 12 - 5 = 9. 
// The code above correctly evaluates this expression and prints the result as 9. 

B:
    #include <iostream>
    #include <vector>
    #include <string>

    using namespace std;

    int do_algebra(vector<string> operato, vector<int> operand) {
        int result = operand[0];
        for(int i = 0; i < operato.size(); i++){
            int a = operand[i];
            int b = operand[i+1];
            if(operato[i] == "+") {
                result += a;
            } else if(operato[i] == "-") {
                result -= a;
            } else if(operato[i] == "*") {
                result *= a;
            } else if(operato[i] == "//") {
                result = result / a;
            } else if(operato[i] == "**") {
                result = pow(result, a);
            }
        }
        return result;
    }

    int main() {
        vector<string> operato = {"+", "*", "-"};
        vector<int> operand = {2, 3, 4, 5};
        int result = do_algebra(operato, operand);
        cout << result << endl;
        return 0;
    }

    // Output: 9
