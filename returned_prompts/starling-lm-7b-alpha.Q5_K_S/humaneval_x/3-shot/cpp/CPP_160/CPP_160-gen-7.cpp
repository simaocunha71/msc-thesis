    int i,j;
    for (i=0;i<operato.size();i++)
    {
        if (operato[i]=="+")
        return do_algebra(operato, operand)+do_algebra(operato, operand);
        if (operato[i]=="-")
        return do_algebra(operato, operand)-do_algebra(operato, operand);
        if (operato[i]=="*")
        return do_algebra(operato, operand)*do_algebra(operato, operand);
        if (operato[i]=="//")
        return do_algebra(operato, operand)//do_algebra(operato, operand);
        if (operato[i]=="^")
        return pow(do_algebra(operato, operand), do_algebra(operato, operand));
    }
    return operand[0];
}







