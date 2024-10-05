    int i;
    int op_size=operato.size();
    int op_operand_size=op_size+1;
    vector<int> new_operand(op_operand_size);
    vector<string> new_operato(op_operand_size);
    new_operand[0]=operand[0];
    new_operato[0]=operato[0];
    i=1;
    while(i<op_size)
    {
        new_operand[i]=operand[i+1];
        new_operato[i]=operato[i+1];
        i++;
    }
    new_operand[i]=operand[op_size];
    new_operato[i]="+";
    i++;
    while(i<op_operand_size-1)
    {
        if (new_operato[i]=="+")
        {
        new_operand[i+1]=new_operand[i]+new_operand[i+2];
        }
        if (new_operato[i]=="-")
        {
        new_operand[i+1]=new_operand[i]-new_operand[i+2];
        }
        if (new_operato[i]=="*")
        {
        new_operand[i+1]=new_operand[i]*new_operand[i+2];
        }
        if (new_operato[i]=="//")
        {
        new_operand[i+1]=new_operand[i]//new_operand[i+2];
        }
        if (new_operato[i]=="**")
        {
        new_operand[i+1]=pow(new_operand[i],new_operand[i+2]);
        }
        i++;
    }
    return new_operand[op_operand_size-1];
}



