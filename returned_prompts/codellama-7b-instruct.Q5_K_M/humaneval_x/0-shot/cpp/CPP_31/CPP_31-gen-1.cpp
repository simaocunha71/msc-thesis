if(n<2) return false;
for(int i=2;i*i<=n;i++){

B:
if(n%i==0) return false;
}
return true;
}
int main()
{
int t;
long long n;
cin>>t;
while(t--)
{
cin>>n;
if(is_prime(n))
{
cout<<"true";
}
else
{
cout<<"false";
}
cout<<endl;
}
return 0;
}
