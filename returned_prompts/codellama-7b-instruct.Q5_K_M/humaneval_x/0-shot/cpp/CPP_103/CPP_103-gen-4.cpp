    if(n>m)
        return "-1";
    int sum = 0;
    int count = 0;
    for(int i=n;i<=m;i++)
    {
        sum += i;
        count ++;
    }
    float avg = sum/count;
    int floor = floor(avg);
    return to_string(floor,2);
}
int main()
{
    int n,m;
    cout<<"Enter the range of numbers: ";
    cin>>n>>m;
    string s = rounded_avg(n,m);
    cout<<"Average is: "<<s<<endl;
    return 0;
}
