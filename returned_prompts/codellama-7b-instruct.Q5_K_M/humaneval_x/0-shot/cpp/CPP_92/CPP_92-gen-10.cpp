if(a+b==c&&a%1==0&&b%1==0&&c%1==0){
return true;
}
else{
return false;
}
}
int main(){
float a,b,c;
printf("Enter 3 numbers: ");
scanf("%f %f %f",&a,&b,&c);
if(any_int(a,b,c)==true){
printf("True\n");
}
else{
printf("False\n");
}

}