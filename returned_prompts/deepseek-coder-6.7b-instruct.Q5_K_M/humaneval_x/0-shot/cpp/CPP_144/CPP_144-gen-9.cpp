    int num1,den1,num2,den2,common_den;
    int i=0;
    while(x[i] != '/'){
        i++;
    }
    num1=stoi(x.substr(0,i));
    den1=stoi(x.substr(i+1));
    i=0;
    while(n[i] != '/'){
        i++;
    }
    num2=stoi(n.substr(0,i));
    den2=stoi(n.substr(i+1));
    common_den=den1*den2;
    num1=num1*den2;
    num2=num2*den1;
    if(num1==num2){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    string x = "1/2";
    string n = "2/1";
    printf("%d",simplify(x,n));
    return 0;
}

In this function, the string is first divided into numerator and denominator and then converted into integer. Then common denominator is calculated and the numerators are multiplied by the denominator of the second fraction. If these two numerators are equal, then the function returns true. Otherwise, it returns false.
*/






























































































































































































