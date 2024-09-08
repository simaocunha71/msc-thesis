    int result = 0;
    int n = operato.size();
    vector<int> stack;
    stack.push_back(operand[0]);
    for(int i = 0; i < n; i++){
        if(operato[i] == "+"){
            stack.push_back(stack.back() + operand[i+1]);
            stack.pop_back();
        }
        else if(operato[i] == "-"){
            stack.push_back(stack.back() - operand[i+1]);
            stack.pop_back();
        }
        else if(operato[i] == "*"){
            stack.push_back(stack.back() * operand[i+1]);
            stack.pop_back();
        }
        else if(operato[i] == "//"){
            stack.push_back(stack.back() / operand[i+1]);
            stack.pop_back();
        }
        else if(operato[i] == "**"){
            stack.push_back(pow(stack.back(), operand[i+1]));
            stack.pop_back();
        }
    }
    return stack[0];
}

int main(){
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    printf("%d\n", do_algebra(operato, operand));
    return 0;
}

