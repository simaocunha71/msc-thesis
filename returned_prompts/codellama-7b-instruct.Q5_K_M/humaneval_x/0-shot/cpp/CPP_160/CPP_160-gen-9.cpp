    int n = operato.size();
    if(n == 0)return 0;
    int i = 0;
    int j = 0;
    int k = 0;
    int m = 0;
    int sum = 0;
    int temp = 0;
    while(k<n){
        switch(operato[k]){
            case "+":
                if(operato.size() == 1){
                    sum = operand[j] + operand[j+1];
                    j = j + 2;
                    break;
                }
                if(operato.size() == 2){
                    sum = operand[j] + operand[j+1];
                    break;
                }
                temp = operand[j] + operand[j+1];
                j = j + 2;
                m = j;
                while(k<n){
                    switch(operato[k]){
                        case "+":
                            sum = temp + operand[j];
                            j = j + 1;
                            break;
                        case "-":
                            sum = temp - operand[j];
                            j = j + 1;
                            break;
                        case "*":
                            sum = temp * operand[j];
                            j = j + 1;
                            break;
                        case "/":
                            sum = temp / operand[j];
                            j = j + 1;
                            break;
                        case "%":
                            sum = temp % operand[j];
                            j = j + 1;
                            break;
                        case "//":
                            sum = temp // operand[j];
                            j = j + 1;
                            break;
                        case "**":
                            sum = pow(temp, operand[j]);
                            j = j + 1;
                            break;
                        default:
                            break;
                    }
                    if(j == m)break;
                }
                break;
            case "-":
                if(operato.size