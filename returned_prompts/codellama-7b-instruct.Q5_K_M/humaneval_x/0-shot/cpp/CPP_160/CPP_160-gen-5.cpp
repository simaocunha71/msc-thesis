    for (int i=0;i<operato.size();i++){
        if (operato[i] == "+"){
            operand[i] += operand[i+1];
            goto B;
        }
        else if (operato[i] == "-"){
            operand[i] -= operand[i+1];
            goto B;
        }
        else if (operato[i] == "*"){
            operand[i] *= operand[i+1];
            goto B;
        }
        else if (operato[i] == "/"){
            operand[i] /= operand[i+1];
            goto B;
        }
        else if (operato[i] == "%"){
            operand[i] %= operand[i+1];
            goto B;
        }
        else if (operato[i] == "^"){
            operand[i] = pow(operand[i], operand[i+1]);
            goto B;
        }
        else if (operato[i] == "//"){
            operand[i] = (int)floor(operand[i]/operand[i+1]);
            goto B;
        }
    }
    return operand[0];
B:
    for(int j=0;j<operato.size();j++){
        if (j==i) continue;
        else{
            if (operato[j] == "+"){
                operand[j] += operand[j+1];
                goto A;
            }
            else if (operato[j] == "-"){
                operand[j] -= operand[j+1];
                goto A;
            }
            else if (operato[j] == "*"){
                operand[j] *= operand[j+1];
                goto A;
            }
            else if (operato[j] == "/"){
                operand[j] /= operand[j+1];
                goto A;
            }
            else if (operato[j]