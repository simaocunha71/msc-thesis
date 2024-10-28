if(a==b+c||b==a+c||c==a+b){
if(a%1==0&&b%1==0&&c%1==0){
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
int main(){
float a,b,c;
cout<<"Enter three numbers\n";
cin>>a>>b>>c;
if(any_int(a,b,c)){
cout<<"Yes\n";
}
else{
cout<<"No\n";
}
}
