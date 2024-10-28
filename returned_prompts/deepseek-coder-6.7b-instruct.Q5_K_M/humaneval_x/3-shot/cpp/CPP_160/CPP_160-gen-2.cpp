    int result = operand[0];
    for (int i = 1; i < operand.size(); i++) {
        if (operato[i-1] == "+") {
            result += operand[i];
        } else if (operato[i-1] == "-") {
            result -= operand[i];
        } else if (operato[i-1] == "*") {
            result *= operand[i];
        } else if (operato[i-1] == "//") {
            result /= operand[i];
