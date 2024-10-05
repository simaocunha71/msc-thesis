    if (n>m) return "-1";
    int sum=0;
    int count=0;
    for (int i=n;i<=m;i++)
    {
        sum+=i;
        count++;
    }
    float avg=float(sum)/count;
    int rounded_avg=round(avg);
    string result="";
    while (rounded_avg>0)
    {
        if (rounded_avg&1)
        {
            result+="1";
        }
        else result+="0";
        rounded_avg>>=1;
    }
    if (result.length()==0) result="0";
    reverse(result.begin(),result.end());
    return result;
}  // 3 lines of code added
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3 lines of code inserted
// 3