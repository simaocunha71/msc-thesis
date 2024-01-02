/*
You are given a vector arr of integers and you need to return
sum of magnitudes of integers multiplied by product of all signs
of each number in the vector, represented by 1, -1 or 0.
Note: return -32768 for empty arr.

Example:
>>> prod_signs({1, 2, 2, -4}) == -9
>>> prod_signs({0, 1}) == 0
>>> prod_signs({}) == -32768
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int prod_signs(vector<int> arr){
	if(arr.size()==0) return -1;
    int *num=new int[arr.size()];
    vector<int>::iterator itt;
    for(int i=0;i<arr.size();++i) num[i]=(arr[i]+1)/2;//multiply arr with 1 and half then take average to calculate magnitude of each number in the vector
	for(itt=num;itt<num+arr.size();++itt){
        if(*(it-1)>0 && *(it)==1) continue; //if its not zero dont check it
        else if (*(it-1)==-1 && *(it)==1) {//if its -1 and 1 then we are done if not find sum of magnitude
            printf("num is %d\n",*(it))*num[i]; //we need to find magnitude of each num
        }else{//if it has no sign 0 then go up and print the value for now but dont save as that would cause error in above step
            printf("%i ",*(it));
		}
    }
	for(int i=0;i<arr.size();++i) prod_signs[i]=(int)(pow((double)(num[i]),3)*1/2);//calculate prod of signs for each number in the vector
    int sum=0;
    for(int i=0;i<prod_signs.size();++i){
        if(!(prod_signs[i]==