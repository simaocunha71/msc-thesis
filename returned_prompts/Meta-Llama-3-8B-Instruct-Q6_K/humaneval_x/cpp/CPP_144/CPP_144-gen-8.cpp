    int num1=0,num2=0,den1=0,den2=0;
    //parse the string to get the numerator and denominator
    int i=0;
    while(x[i]!='/'){
        num1=num1*10+(x[i]-'0');
        i++;
    }
    den1=atoi(&x[i+1]);
    
    i=0;
    while(n[i]!='/'){
        num2=num2*10+(n[i]-'0');
        i++;
    }
    den2=atoi(&n[i+1]);
    
    //simplify the fraction
    int gcd = __gcd(num1*den2,num2*den1);
    num1 = num1*den2/gcd;
    den1 = num2*den1/gcd;
    
    //check if the simplified fraction is a whole number
    if(den1==1 && num1==0){
        return true;
    }
    return false;
}

int main()
{
    printf("%d\n",simplify("1/5", "5/1"));
    printf("%d\n",simplify("1/6", "2/1"));
    printf("%d\n",simplify("7/10", "10/2"));
    return 0;
}
