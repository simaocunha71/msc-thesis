    if (decimal==0){
        return "db0db";
    }
    else{
        int binary=0;
        int i;
        for (i=0;i<decimal;i++){
            binary*=2;
            binary+=1;
        }
        string binary_str;
        for (i=binary;i>0;i/=2){
            if (i%2==0)
            binary_str+='0';
            if (i%2==1)
            binary_str+='1';
        }
        return "db"+binary_str+"db";
    }
}



