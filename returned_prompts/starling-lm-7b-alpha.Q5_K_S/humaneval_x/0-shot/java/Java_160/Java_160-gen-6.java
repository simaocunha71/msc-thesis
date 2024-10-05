        while(operator.size()!=0){
            int i=0;
            for(i=0;i<operator.size();i++){
                if(operator.get(i).equals("+")){
                    operand.set(i,operand.get(i-1)+operand.get(i));
                    operator.remove(i);
                    operand.remove(i-1);
                    continue A;
                }
                if(operator.get(i).equals("-")){
                    operand.set(i,operand.get(i-1)-operand.get(i));
                    operator.remove(i);
                    operand.remove(i-1);
                    continue A;
                }
                if(operator.get(i).equals("*")){
                    operand.set(i,operand.get(i-1)*operand.get(i));
                    operator.remove(i);
                    operand.remove(i-1);
                    continue A;
                }
                if(operator.get(i).equals("/")){
                    operand.set(i,operand.get(i-1)/operand.get(i));
                    operator.remove(i);
                    operand.remove(i-1);
                    continue A;
                }
                if(operator.get(i).equals("**")){
                    operand.set(i,operand.get(i-1)**operand.get(i));
                    operator.remove(i);
                    operand.remove(i-1);
                    continue A;
                }
            }
        }
        return operand.get(0);
    }
}










    
    
    


    
    
    



















































    




























