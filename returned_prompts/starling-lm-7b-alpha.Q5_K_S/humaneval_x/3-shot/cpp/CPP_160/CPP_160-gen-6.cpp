    vector<string> all_operations;
    vector<int> all_operands;
    int i;
    int result=0;
    int length_o=operato.size();
    int length_op=operand.size();
    for (i=0;i<length_op-1;i++)
    {
        all_operands.push_back(operand[i]);
        if (length_o!=0){
        all_operations.push_back(operato[i]);
        }
    }
    all_operands.push_back(operand[length_op-1]);
    sort(all_operands.begin(),all_operands.end());
    if (all_operations.size()==0){
    result=all_operands[0];
    }
    if (all_operations.size()==1){
    if (all_operations[0]=="*"){
        result=all_operands[0]*all_operands[1];
    }
    if (all_operations[0]=="//"){
        result=all_operands[0]//all_operands[1];
    }
    }
    if (all_operations.size()==2){
    if (all_operations[0]=="+" && all_operations[1]=="-"){
        result=all_operands[0]+all_operands[1];
    }
    if (all_operations[0]=="*" && all_operations[1]=="+"){
        result=all_operands[0]*all_operands[1];
    }
    }
    if (all_operations.size()==3){
    if (all_operations[0]=="+" && all_operations[1]=="-" && all_operations[2]=="+"){
        result=all_operands[0]+all_operands[1]+all_operands[2];
    }
    }
    return result;
}








































