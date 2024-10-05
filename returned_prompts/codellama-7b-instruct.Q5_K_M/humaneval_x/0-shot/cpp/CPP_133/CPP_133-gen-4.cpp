    int sum=0;
    for(int i=0;i<lst.size();i++)
    {
        sum+=(int)pow(ceil(lst[i]),2);
    }
    return sum;

}
int main()
{
    vector<float>lst={1.4,4.2,0};
    printf("%d",sum_squares(lst));
    return 0;
}
