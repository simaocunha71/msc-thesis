    if(b == 0){
        return a;
    }
    else{
        return greatest_common_divisor(b, a % b);
    }
}

int main(){
    int a, b;
    cout<<"Enter two integers: ";
    cin>>a>>b;
    cout<<"The greatest common divisor is "<<greatest_common_divisor(a, b);
    return 0;
}

//