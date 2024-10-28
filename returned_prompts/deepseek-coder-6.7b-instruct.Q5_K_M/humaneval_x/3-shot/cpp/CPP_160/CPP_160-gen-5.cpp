    int i,res = operand[0];
    for(i=0;i<operato.size();i++)
    {
        if(operato[i] == "+")
            res += operand[i+1];
        else if(operato[i] == "-")
            res -= operand[i+1];
        else if(operato[i] == "*")
            res *= operand[i+1];
        else if(operato[i] == "//")
            res /= operand[i+1];
        else if(operato[i] == "**")
            res = pow(res,operand[i+1]);
    }
    return res;
}


