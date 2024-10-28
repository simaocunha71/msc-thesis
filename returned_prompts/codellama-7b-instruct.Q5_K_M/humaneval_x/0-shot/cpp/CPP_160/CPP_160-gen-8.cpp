    for(int i=0;i<operato.size();i++){
        if(operato[i]=="+"){
            operand[i+1]+=operand[i];
            operand.erase(operand.begin()+i);
            operato.erase(operato.begin()+i);
            goto A;
        }
        if(operato[i]=="-"){
            operand[i+1]-=operand[i];
            operand.erase(operand.begin()+i);
            operato.erase(operato.begin()+i);
            goto A;
        }
        if(operato[i]=="*"){
            operand[i+1]*=operand[i];
            operand.erase(operand.begin()+i);
            operato.erase(operato.begin()+i);
            goto A;
        }
        if(operato[i]=="/"){
            operand[i+1]/=operand[i];
            operand.erase(operand.begin()+i);
            operato.erase(operato.begin()+i);
            goto A;
        }
        if(operato[i]=="^"){
            operand[i+1]=pow(operand[i],operand[i+1]);
            operand.erase(operand.begin()+i);
            operato.erase(operato.begin()+i);
            goto A;
        }
    }
    return operand[operand.size()-1];
}
int main(){
    int n,m;
    cin>>n>>m;
    vector<string> operato(n-1);
    vector<int> operand(m);
    for(int i=0;i<n-1;i++){
        cin>>operato[i];
    }
    for(int i=0;i<m;i++){
        cin>>operand[i];
    }
    int result=do_algebra(operato,operand);
    cout<<result;
    return