if(a==b+c)
return true;
else
return false;

}

int main(){
float a,b,c;
scanf("%f%f%f",&a,&b,&c);
if(any_int(a,b,c)==true)
printf("true");
else
printf("false");
}
