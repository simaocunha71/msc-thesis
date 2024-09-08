/*
Write a program that uses a while loop to find and print the largest divisor of a number
*/
int i=1;
while(i<n)
{
if(n%i==0)
{
printf("%d",i);
}
i++;
}
return 0;
}
B:
/*
Write a program that uses a for loop to find and print the largest divisor of a number
*/
int largest_divisor(int n){
int i;
for(i=1;i<n;i++)
{
if(n%i==0)
{
printf("%d",i);
}
}
return 0;
}
C:
/*
Write a function that takes a number as an argument and returns the largest divisor of that number
*/
int largest_divisor(int n){
int i;
int max_divisor=1;
for(i=1;i<n;i++)
{
if(n%i==0)
{
max_divisor=i;
}
}
return max_divisor;
}
D:
/*
Write a function that takes a number as an argument and returns the largest divisor of that number, excluding 1 and the number itself
*/
int largest_divisor(int n){
int i;
int max_divisor=1;
for(i=2;i<n-1;i++)
{
if(n%i==0)
{
max_divisor=i;
}
}
return max_divisor;
}
E:
/*
Write a function that takes a number as an argument and returns the largest divisor of that number, excluding 1, the number itself, and any prime numbers
*/
int largest_divisor(int n){
int i;
int max_divisor=1;
for(i=2;i<n-1;i++)
{
if(n%i==0)
{
max_divisor=i;
}
}
return max_divisor;
}
F:
/*
Write a function that takes a number as an argument and returns the largest divisor of that number, excluding 1, the number itself, and any prime numbers, and also returns the count of the number of divisors found
*/
int largest_divisor(int n){
int i;
int max_divisor=1;
int count=0;
for(i=2;i<n-1;i++)
{
if(n%i==0)
{
max_divisor=i;
count++;
}
}
return max_divisor;
}
G:
/*
Write a function that takes a number as an argument and returns the largest divisor of that number, excluding 1, the number itself, and any prime numbers, and also returns the count of the number of divisors found, and also returns the list of all divisors found
*/
int