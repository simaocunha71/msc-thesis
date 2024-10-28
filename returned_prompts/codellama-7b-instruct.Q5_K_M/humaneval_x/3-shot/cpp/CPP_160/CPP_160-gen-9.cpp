    int i,j;
    vector<string> operato_cpy = operato;
    vector<int> operand_cpy = operand;
    int result = operand_cpy[0];
    for (i=0;i<operato.size();i++)
    {
        switch (operato[i])
        {
            case "+":
                result+= operand_cpy[i+1];
                break;
            case "-":
                result-= operand_cpy[i+1];
                break;
            case "*":
                result*= operand_cpy[i+1];
                break;
            case "/":
                result/= operand_cpy[i+1];
                break;
            case "%":
                result%= operand_cpy[i+1];
                break;
            case "^":
                result = (int) pow(result, operand_cpy[i+1]);
                break;
        }
    }
    return result;
}


