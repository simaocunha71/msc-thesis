/*
Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

This function outputs the number of such collisions.
*/
#include<stdio.h>
using namespace std;
int car_race_collision(int n){
	int c=0;
	for (int i=1 ;i<=n-1;i++){  //for i=i+2
		int temp = i + 1, c1 = i + 1, c2 = n - 1;
    	c+=i % 2 == 0 ? (c1 - temp) :(temp - c1);
    }
    return c; 
}
int main(){
    int n=9;
   printf("n is%d\n",n);
   printf("%d\n",car_race_collision(n));
	return 0;
}