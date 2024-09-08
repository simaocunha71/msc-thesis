    int n = operato.size();
    if(n < 1 || n > operand.size() - 1){
        printf("Invalid input\n");
        return -1;
    }
    int i = 0;
    int j = 0;
    string temp;
    vector<int> res;
    for(int i = 0; i < operand.size(); i++){
        while(j < n){
            if(j == n - 1){
                res.push_back(operand[i]);
                break;
            }
            if(operato[j] == "+"){
                res.push_back(operand[i]);
                j++;
            }else if(operato[j] == "-"){
                res.push_back(-operand[i]);
                j++;
            }else if(operato[j] == "*"){
                if(res.size() > 0) res.back() *= operand[i];
                else res.push_back(operand[i]);
                j++;
            }else if(operato[j] == "//"){
                if(res.size() > 0) res.back() /= operand[i];
                else res.push_back(operand[i]);
                j++;
            }else if(operato[j] == "**"){
                if(res.size() > 0) res.back() = pow(res.back(), operand[i]);
                else res.push_back(operand[i]);
                j++;
            }
        }
    }
    int result = 0;
    for(int i = 0; i < res.size(); i++){
        result += res[i];
    }
    return result;
}
int main() {
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    int result = do_algebra(operato, operand);
    printf("Result: %d\n", result);
    return 0;
}

S:
    The given problem is solved using a simple algorithm. The program iterates through the operator and operand vectors. It checks the current operator and performs the corresponding operation on the result. The result is stored in the result vector. After all the operators are processed, the result vector is iterated to get the final result. The final result is the sum of all the elements in the result vector.

    The given problem is solved using a simple algorithm. The program iterates through the operator and operand vectors. It checks the current operator and performs the corresponding operation on the result. The result is stored in the result vector. After all the operators are processed, the