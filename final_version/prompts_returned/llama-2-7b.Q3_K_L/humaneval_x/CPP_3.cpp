/*
You"re given a vector of deposit and withdrawal operations on a bank account that starts with
zero balance. Your task is to detect if at any point the balance of account falls below zero, and
at that point function should return true. Otherwise it should return false.
>>> below_zero({1, 2, 3})
false
>>> below_zero({1, 2, -4, 5})
true
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool below_zero(vector<int> operations){
	if(operations[0]==-1)
	{return true;}else if(operations[operations.size()-1]!=1)
		{return false;}
}
int main(){
	vector<int> operations;
	int choice,deposit=0,withdrawal=-1,result=0;
	do{
		printf("Enter your choice\n");
		scanf("%d",&choice);
		if(choice==1)
		{
			printf("Enter your deposit amount\n");
			scanf("%d",&deposit);
		}else if(choice==2)
		{
			printf("Enter your withdrawal amount\n");
			scanf("%d",&withdrawal);
		}else
		{ printf("Wrong input,try again\n"); }
		operations.push_back(deposit);
		if(choice==1)
			{operations.push_back(-1);}else if(choice==2){operations.pop_back();}
	}while(choice!=0&&choice!=3);
int main()
{
	for(int i=0;i<operations.size();++i)
	printf("%d ",operations[i]);
}
