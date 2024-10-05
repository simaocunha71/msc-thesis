    int i;
    int len=operand.size();
    vector<string>::iterator it;
    vector<int>::iterator it2;
    vector<int> tmp;
    for (i=0;i<len;i++)
    {
    it=lower_bound(operato.begin(), operato.end(), operato[i]);
    if (it!=operato.begin())
    {
    int v=*prev(it);
    if (v=='*')
    {
    tmp.push_back(operand[i-1]*operand[i]);
    it2=next(tmp.begin());
    while (it2!=tmp.end())
    {
    operand.erase(it2);
    tmp.push_back(*it2);
    it2=next(tmp.begin());
    }
    }
    if (v=='/')
    {
    tmp.push_back(operand[i-1]//operand[i]);
    it2=next(tmp.begin());
    while (it2!=tmp.end())
    {
    operand.erase(it2);
    tmp.push_back(*it2);
    it2=next(tmp.begin());
    }
    }
    }
    }
    return operand[i-1];
}


int main(){
    vector<float> numbers={1.0, 2.0, 3.0};
    vector<string> operato={"+", "*", "-"};
    vector<int> operand={2, 3, 4, 5};
    printf("%.2f\n", truncate_number(3.5));
    printf("%d\n", has_close_elements(numbers, 0.5));
    printf("{");
    for (auto s: separate_paren_groups("( ) (( )) (( )( ))"))
    {
        printf("%s,", s.c_str());
    }
    printf("}\n");
    printf("%d\n", do_algebra(operato, operand));
    return 0;
}
















