    int a = operand.back();
    operand.pop_back();
    int b = operand.back();
    operand.pop_back();

    if(operato.back() == "+"){
        operand.push_back(a + b);
    }
    else if(operato.back() == "-"){
        operand.push_back(a - b);
    }
    else if(operato.back() == "*"){
        operand.push_back(a * b);
    }
    else if(operato.back() == "//"){
        operand.push_back(a / b);
    }
    else if(operato.back() == "**"){
        operand.push_back(pow(a, b));
    }
    goto A;
}

vector<int> operands;
vector<string> operators;
int result;
int main()
{
    string in;
    int i = 0;
    while(cin >> in){
        if(in == "+"){
            operators.push_back(in);
        }
        else if(in == "-"){
            operators.push_back(in);
        }
        else if(in == "*"){
            operators.push_back(in);
        }
        else if(in == "//"){
            operators.push_back(in);
        }
        else if(in == "**"){
            operators.push_back(in);
        }
        else{
            operands.push_back(atoi(in.c_str()));
        }
    }
    result = do_algebra(operators, operands);
    printf("%d\n", result);
}



*/



































































































