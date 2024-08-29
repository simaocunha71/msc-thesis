vector<int> v={};
vector<int> v1={};
int sum=0;
int product=1;
for(int i=0;i<numbers.size();i++)
{
if(numbers[i]==0)
{
sum+=0;
product*=1;
}
else
{
sum+=numbers[i];
product*=numbers[i];
}
}
v