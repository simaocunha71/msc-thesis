    if (lst.size()==0)
        return 0;
    float sum = 0;
    for (int i = 0; i < lst.size(); i++)
    {
        if (lst[i]<0 || !(lst[i]==(int)lst[i]))
            continue;
        if (lst[i]%2==0)
            continue;
        sum += pow(lst[i],2);
    }
    return sum;
}
int main(){
    vector<float> lst{1,3,2,0};
    printf("%lld", double_the_difference(lst));
    return 0;
}

Ans: CORRECT

