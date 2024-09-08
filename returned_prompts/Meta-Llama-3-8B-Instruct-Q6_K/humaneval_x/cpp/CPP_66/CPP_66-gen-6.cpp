    int sum=0;
    for(int i=0;i<s.size();i++){
        if(isupper(s[i])){
            sum+=s[i];
        }
    }
    return sum;
}
int main(){
    string s;
    printf("Enter the string\n");
    getline(cin,s);
    printf("The sum of upper characters ASCII code is %d\n",digitSum(s));
    return 0;
}
