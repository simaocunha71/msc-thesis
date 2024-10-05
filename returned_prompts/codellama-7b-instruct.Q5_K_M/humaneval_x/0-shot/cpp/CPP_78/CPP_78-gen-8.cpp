
int hex_key(string num){

    int hex_key=0;
    if(num.length()==0)
        return hex_key;

    int hex[16]={0,1,2,3,4,5,6,7,8,9,0,0,0,0,0,0};
    string prime[16]={"2","3","5","7","B","D","11","13","17","19","23","29","31","37","41","43"};

    for(int i=0;i<num.length();i++){
        for(int j=0;j<16;j++){
            if(num[i]==prime[j][0]){
                hex_key++;
                break;
            }
        }
    }
    return hex_key;
}

