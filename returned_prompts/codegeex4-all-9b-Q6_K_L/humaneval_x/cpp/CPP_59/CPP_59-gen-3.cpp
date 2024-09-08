int i=2;
while(n%i==0)
{
n=n/i;
}
return n;
}
B:
int largest_prime_factor(int n){
for(int i=2;i<=n;i++)
{
if(n%i==0)
{
n=n/i;
return i;
}
}
return n;
}
C:
int largest_prime_factor(int n){
while(n%2==0)
{
n=n/2;
}
for(int i=3;i*i<=n;i+=2)
{
if(n%i==0)
{
n=n/i;
return i;
}
}
return n;
}
D:
int largest_prime_factor(int n){
int max=-1;
for(int i=2;i<=n;i++)
{
if(n%i==0)
{
max=max>i?max:i;
n=n/i;
}
}
return max;
}
E:
int largest_prime_factor(int n){
while(n%2==0)
{
n=n/2;
}
for(int i=3;i*i<=n;i+=2)
{
if(n%i==0)
{
n=n/i;
return i;
}
}
return n;
}
F:
int largest_prime_factor(int n){
int max=-1;
while(n%2==0)
{
n=n/2;
}
for(int i=3;i*i<=n;i+=2)
{
if(n%i==0)
{
max=max>i?max:i;
n=n/i;
}
}
return max;
}
G:
int largest_prime_factor(int n){
int max=-1;
while(n%2==0)
{
n=n/2;
}
for(int i=3;i*i<=n;i+=2)
{
if(n%i==0)
{
max=max>i?max:i;
n=n/i;
}
}
return max;
}
H:
int largest_prime_factor(int n){
int max=-1;
while(n%2==0)
{
n=n/2;
}
for(int i=3;i*i<=n;i+=2)
{
if(n%i==0)
{
max=max>i?max:i;
n=n/i;
}
}
return max;
}
I:
int largest_prime_factor(int n){
int max=-1;
while(n%2==0)
{
n=n/2;
}
for(int i=3;i*i<=n;i+=2)
{
if(n%i==0)
{
max=max>i?max:i;
n=n/i;
}
}
return max;
}
J:
int largest_prime_factor(int n){
int max=-1;
while(n%2==0)
{
n=n