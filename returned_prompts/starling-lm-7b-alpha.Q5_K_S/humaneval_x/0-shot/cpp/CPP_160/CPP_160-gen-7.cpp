    int l = operato.size();
    int m = operand.size();
    if(l != m-1){
        return -1;
    }
    int i = 0, j = 0, k = 0;
    int sum = 0;
    while(k < l){
        if(operato[i] == "+"){
            sum += operand[j];
            j++;
        }else if(operato[i] == "*"){
            sum *= operand[j];
            j++;
        }else if(operato[i] == "-"){
            sum -= operand[j];
            j++;
        }else if(operato[i] == "//"){
            sum /= operand[j];
            j++;
        }else if(operato[i] == "**"){
            sum = pow(sum, operand[j]);
            j++;
        }
        i++;
        k++;
    }
    return sum;
}
int main(){
    vector<string> operato;
    vector<int> operand;
    string s;
    int n, t;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        cin >> s;
        operato.push_back(s);
    }
    for(int i = 0; i < n; i++){
        scanf("%d", &t);
        operand.push_back(t);
    }
    printf("%d\n", do_algebra(operato, operand));
    return 0;
}

*/




































































































































