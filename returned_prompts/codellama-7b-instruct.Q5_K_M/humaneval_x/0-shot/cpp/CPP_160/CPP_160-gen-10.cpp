    if (operato.size()==0){
        return operand[0];
    }
    if (operato.size()==1){
        if (operato[0]=="+"){
            return operand[0]+operand[1];
        }
        if (operato[0]=="-"){
            return operand[0]-operand[1];
        }
        if (operato[0]=="*"){
            return operand[0]*operand[1];
        }
        if (operato[0]=="/"){
            return operand[0]/operand[1];
        }
        if (operato[0]=="**"){
            return pow(operand[0], operand[1]);
        }
        if (operato[0]=="%"){
            return operand[0]%operand[1];
        }
    }
    if (operato.size()==2){
        if (operato[0]=="+"){
            return operand[0]+operand[1]+operand[2];
        }
        if (operato[0]=="-"){
            return operand[0]-operand[1]-operand[2];
        }
        if (operato[0]=="*"){
            return operand[0]*operand[1]*operand[2];
        }
        if (operato[0]=="/"){
            return operand[0]/operand[1]/operand[2];
        }
        if (operato[0]=="**"){
            return pow(operand[0], operand[1])*pow(operand[2], operand[2]);
        }
        if (operato[0]=="%"){
            return operand[0]%operand[1]%operand[2];
        }
    }
    if (operato.size()==3){
        if (operato[0]=="+"){
            return operand[0]+operand[1]+operand[2]+operand[3];
        }
        if (operato[0]=="-"){
           