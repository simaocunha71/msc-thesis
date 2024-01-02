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
	int x=0,y=0,z=n-2;
	while (x<=1) {
	if ((z==1) && (y==0))
	printf("Car collision \n");
	if (z!=0) {
    y++;
  if (z>0) {
    x++;
      z--;
     }
   }
  else{

     x++;
       return 1;
  }
}
return 1;

}
int main(){
	printf("Car collision \n");
	int n=5;
	car_race_collision(n);
	return 0;
}