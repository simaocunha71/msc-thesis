/*
Given length of a side and high return area for a triangle.
>>> triangle_area(5, 3)
7.5
*/
#include<stdio.h>
#include<math.h>
using namespace std;
float triangle_area(float a,float h){
    float res=0;
    if(a<=1||sqrt(pow(a,2)-pow((h/2), 2)) <= 1)//check for valid input
        return -1;
    else{
        //compute area and pi
        res=1/(3*tan(atan(h/2.0f)/3.0));
         printf("Area is : %.4f\n",res);    
    }
}
int main(){
    int choice,ch;
    float temp[15];
    char option='a';
    do{
        printf("\nEnter 1 to calculate area of triangle\n");
        printf("2 to calculte sides of a triangle\n");
        printf("3 to exit program\nEnter your choice: ");
        scanf("%d",&choice);
        switch(choice){
            case 1:{
                for(int i=0;i<=14 ; i++){
                    printf("\nEnter sides of a triangle \n");
                    printf("Press key to enter value\ntype 'q' to quit ");
                    scanf("%d",&temp[i]);
                    while(scanf("%c",&ch)!=EOF && ch!='e'){ //loop while user is not entered 'e'
                        if (scanf("%c",&ch)==1){
                            printf("\nEntered value for side %d is : ",i);
                            printf("enter the right value\n");
                            scanf("%d",&temp[i]);
                            }
                }
                if(scanf("%c",&ch)==1){ //check for valid input when user enter 'e' to quit program
                    printf("\nProgram end ");
                    break;
                }
                   else{printf("Invalid input ");continue;} 
            }
            case 2:{
                     float sum=0,i=0;
                    