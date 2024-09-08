/*
The input is guaranteed to be in the range 0 to 10000.
*/
int i,j;
int a[10000],b[10000];
for(i=0;i<n;i++)
    scanf("%d",&a[i]);
for(i=0;i<n;i++)
    scanf("%d",&b[i]);
int p=0,q=0;
while(p<n && q<n)
{
    if(a[p]>b[q])
    {
        p++;
    }
    else if(a[p]<b[q])
    {
        q++;
    }
    else
    {
        p++;q++;
    }
}
return p+q;
}
int main()
{
    int n;
    scanf("%d",&n);
    printf("%d",car_race_collision(n));
    return 0;
}

C:
/*
Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two