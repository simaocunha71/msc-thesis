    int b = (int)pow(a, 1/3);
    if(b*b*b == a){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    int a = -1;
    if(iscuber(a)){
        printf("The value is true\n");
    }
    else{
        printf("The value is false\n");
    }
    return 0;
}

