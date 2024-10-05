    if(a==(b+c) && a==(int)a && b==(int)b && c==(int)c){
        return true;
    }
    else{
        return false;
    }

}
int main(){
    float a,b,c;
    cin>>a>>b>>c;
    if(any_int(a,b,c)==true){
        cout<<"true";
    }
    else{
        cout<<"false";
    }
    return 0;
}
