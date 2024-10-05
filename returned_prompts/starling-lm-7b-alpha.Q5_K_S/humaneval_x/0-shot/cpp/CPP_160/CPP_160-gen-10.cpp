    int t=operato.size();
    int result=operand[0];
    for(int i=0;i<t;i++){
        if(operato[i]=="+") result+=operand[i+1];
        if(operato[i]=="-") result-=operand[i+1];
        if(operato[i]=="*") result*=operand[i+1];
        if(operato[i]=="//") result/=operand[i+1];
        if(operato[i]=="**") result=pow(result, operand[i+1]);
        i++;
    }
    return result;
}
vector<string> operator_;
vector<int> operand_;
int main(){
    int n;
    scanf("%d",&n);
    scanf("%*c");
    char c;
    for(int i=0;i<n-1;i++){
        scanf("%c",&c);
        operator_.push_back(c);
        scanf("%*c");
    }
    scanf("%d",&n);
    scanf("%*c");
    for(int i=0;i<n;i++){
        scanf("%d",&n);
        operand_.push_back(n);
    }
    int result=do_algebra(operator_, operand_);
    printf("%d\n", result);
    return 0;
}

*/



































































































































































