    if (n>m) return "-1";
    int sum=0;
    for (int i=n;i<=m;i++)
    sum+=i;
    float avg=sum/(float)(m-n+1);
    int rounded_avg=(int)round(avg);
    string binary;
    while (rounded_avg>0)
    {
        if (rounded_avg%2==1)
        binary="1"+binary;
        else
        binary="0"+binary;
        rounded_avg/=2;
    }
    return binary;
}
//test
int main()
{
    printf("%s\n",rounded_avg(1,5).c_str());
    printf("%s\n",rounded_avg(7,5).c_str());
    printf("%s\n",rounded_avg(10,20).c_str());
    printf("%s\n",rounded_avg(20,33).c_str());
    return 0;
}
//test end
*/












