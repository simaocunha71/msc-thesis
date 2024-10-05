
int main(){
    string s;
    int n;
    while(scanf("%s",&s)!=EOF){
        scanf("%d",&n);
        int count=0;
        int mango=0;
        string::size_type size=s.size();
        for(int i=0;i<size;i++){
            if(s[i]=='m'||s[i]=='a'||s[i]=='n'||s[i]=='g'||s[i]=='o')
                count++;
            else if(s[i]=='a'||s[i]=='n'||s[i]=='g')
                mango++;
        }
        printf("the number of fruits in the basket is %d\n",count);
        printf("the number of mango fruits in the basket is %d\n