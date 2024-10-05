if(a==b+c||b==a+c||c==a+b){
    if(a==round(a)&&b==round(b)&&c==round(c)){
        return true;
    }
    else{
        return false;
    }
}
else{
    return false;
}

}

int main()
{
    float a,b,c;
    bool result;
    scanf("%f %f %f",&a,&b,&c);
    result=any_int(a,b,c);
    if(result==true){
        printf("true");
    }
    else{
        printf("false");
    }
    
    return 0;
}
