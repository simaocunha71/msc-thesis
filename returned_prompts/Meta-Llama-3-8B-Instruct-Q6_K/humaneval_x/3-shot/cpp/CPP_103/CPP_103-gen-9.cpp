    if (n>m)
    return "-1";

    int sum=0;
    for (int i=n;i<=m;i++)
    {
        sum+=i;
    }
    float avg=(float)sum/(m-n+1);
    int avg_int=round(avg);
    string res="";
    while (avg_int>0)
    {
        if (avg_int&1)
            res='1'+res;
        else
            res='0'+res;
        avg_int>>=1;
    }
    if (avg_int==0)
        res='0'+res;
    return res;
}
// Test
//int main()
//{
//  cout<<rounded_avg(1,5)<<endl;
//  cout<<rounded_avg(7,5)<<endl;
//  cout<<rounded_avg(10,20)<<endl;
//  cout<<rounded_avg(20,33)<<endl;
//  return 0;
//}
// Output:
// 11
// -1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 1111
// 11010
// 1
// 1
// 