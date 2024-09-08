    // Build the expression from the operator and operand vectors
    string expression = "";
    for(int i = 0; i < operato.size(); i++){
        expression += to_string(operand[i]);
        expression += operato[i];
    }
    expression += to_string(operand[operato.size()]);

    // Evaluate the expression
    int result = 0;
    try {
        result = std::stoi(expression);
    } catch (const std::invalid_argument& e) {
        // handle the exception
        printf("Invalid expression.\n");
    }
    return result;
}
int main() {
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    printf("%d\n", do_algebra(operato, operand));
    return 0;
}

