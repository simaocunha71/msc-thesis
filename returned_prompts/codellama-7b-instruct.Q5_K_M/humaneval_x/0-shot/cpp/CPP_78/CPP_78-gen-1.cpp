if(num[0]=='A'){
if(num[1]=='B'){

B:
if(num[2]=='D'){

D:
if(num=='1'|| num=='2'|| num=='3'|| num=='5'|| num=='7'){
return 1;
}
else{
return 0;
}
}
else{
return 0;
}
}
else{
return 0;
}
}
else{
return 0;
}
}

int hex_primes(string num){
int count=0;
for(int i=0;i<num.length();i++){
if(num[i]=='A'||num[i]=='B'||num[i]=='C'||num[i]=='D'||num[i]=='E'||num[i]=='F'){
count+=hex_key(num