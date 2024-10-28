	int sum = 0;
	for(int i = 0; i < lst.size(); i++){
		if(i % 2 == 0 && lst[i] % 2 != 0){
			sum += lst[i];
		}
	}
	return sum;
}

int main(){
	vector<int> lst = {5, 8, 7, 1};
	printf("%d\n",solutions(lst));
	return 0;
}











*/
#include<stdio.h>
#include<vector>
using namespace std;

int solutions(vector<int> lst){
	int sum = 0;
	for(int i = 0; i < lst.size(); i++){
		if(i % 2 == 0 && lst[i] % 2 != 0){
			sum += lst[i];
		}
	}
	return sum;
}

int main(){
	vector<int> lst = {3, 3, 3, 3, 3};
	printf("%d\n",solutions(lst));
	return 0;
}
























































































































































































































