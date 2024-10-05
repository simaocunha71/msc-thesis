	for(int i = 0; i < arr.size(); i++)
		if(arr[i] > arr[i-1]){
			for(int j = i-1; j >= 0; j--)
				if(arr[i] > arr[j])
					continue A;
			return i;
		}
	return -1;
}
int main() {
	vector<int> arr;
	arr.push_back(1);
	arr.push_back(2);
	arr.push_back(4);
	arr.push_back(3);
	arr.push_back(5);
	printf("%d",can_arrange(arr));
	return 0;
}


*/

#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<int> arr;
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		int a;
		cin>>a;
		arr.push_back(a);
	}
	cout<<can_arrange(arr);
	return 0;
}

int can_arrange(vector<int> arr) {
	for (int i = 1; i < arr.size(); i++)
		if (arr[i] < arr[i - 1])
			for (int j = i - 1; j >= 0; j--)
				if (arr[i] < arr[j])
					return j;
	return -1;
}

















































































































