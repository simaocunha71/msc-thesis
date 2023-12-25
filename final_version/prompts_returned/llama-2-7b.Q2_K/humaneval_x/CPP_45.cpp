/*
Given length of a side and high return area for a triangle.
>>> triangle_area(5, 3)
7.5
*/
#include<stdio.h>
#include<math.h>
using namespace std;
float triangle_area(float a,float h){
    float base=a*sqrtf(1+powf((double)(-1),2));
    if (base<=0) 
        return 0.;
    else
        return powf(base,3)/4.*h;
}
int main(){
	float res, a, h, v;
	scanf("%d %d",&a,&h);
	if((v=triangle_area(a,h))>0. && fabs(v)>1e-6){
	    printf("triangle area=%f\n",res=v);
	}else 
		printf("error: triangle area is not defined\n");
	return 0;
}