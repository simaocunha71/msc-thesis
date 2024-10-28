
1. Your first code snippet is correct.

2. Your second code snippet has a logical error. The following code should be:
if (chr=='(')
{
    level+=1;
    current_paren+=chr;
}
else if (chr==')')
{
    level-=1;
    current_paren+=chr;
    if (level==0){
        all_parens.push_back(current_paren);
        current_paren="";
    }
}

3. Your third code snippet is correct.

4. Your fourth code snippet has a logical error. The following code should be:
int i;
int sum=operand[0];
for (i=0;i<operato.size();i++)
{
    if (operato[i]=="+")
        sum+=operand[i+1];
    else if (operato[i]=="-")
        sum-=operand[i+1];
    else if (operato[i]=="*")
        sum*=operand[i+1];
    else if (operato[i]=="//")
        sum/=operand[i+1];
    else if (operato[i]=="**")
        sum=pow(sum,operand[i+1]);
}
return sum;