    return (a%10)*(b%10);
}
// or
int multiply(int a,int b){
    return (a%10)*(b%10);
}
// or
int multiply(int a,int b){
    return ((a%10)*(b%10));
}
// or
int multiply(int a,int b){
    return (a%10)*(b%10);
} // end of multiply function
// The unit digit of a number is the remainder when divided by 10
// So we just need to take the remainder of a and b when divided by 10
// Then multiply these two remainder together. This is the product of their unit digits. 

