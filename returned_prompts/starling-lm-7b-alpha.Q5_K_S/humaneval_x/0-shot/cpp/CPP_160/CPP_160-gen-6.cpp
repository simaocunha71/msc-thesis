	if(operato.size()==0)
		return operand[0];
	else if(operato[0]=="+"){
		int a = operand[0];
		operando.erase(operando.begin());
		operato.erase(operato.begin());
		int b = do_algebra(operato, operand);
		return a+b;
	}
	else if(operato[0]=="-"){
		int a = operand[0];
		operando.erase(operando.begin());
		operato.erase(operato.begin());
		int b = do_algebra(operato, operand);
		return a-b;
	}
	else if(operato[0]=="*"){
		int a = operand[0];
		operando.erase(operando.begin());
		operato.erase(operato.begin());
		int b = do_algebra(operato, operand);
		return a*b;
	}
	else if(operato[0]=="//"){
		int a = operand[0];
		operando.erase(operando.begin());
		operato.erase(operato.begin());
		int b = do_algebra(operato, operand);
		return a/b;
	}
	else if(operato[0]=="**"){
		int a = operand[0];
		operando.erase(operando.begin());
		operato.erase(operato.begin());
		int b = do_algebra(operato, operand);
		return pow(a, b);
	}
	return -1;
}
int main(){
	vector<string> operato;
	vector<int> operand;
	string a;
	int b, i=0;
	scanf("%s", &a);
	while(a[i]!='\0'){
		operato.push_back(a[i]);
		i++;
	}
	scanf("%d", &b);
	while