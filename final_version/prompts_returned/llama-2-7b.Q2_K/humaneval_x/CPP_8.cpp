/*
For a given vector of integers, return a vector consisting of a sum and a product of all the integers in a vector.
Empty sum should be equal to 0 and empty product should be equal to 1.
>>> sum_product({})
(0, 1)
>>> sum_product({1, 2, 3, 4})
(10, 24)
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> sum_product(vector<int> numbers){
	if(numbers.size()==0){
		return vector < int > ();
	}
	else{
		vector < double > ans=sum_product2(numbers);
		vector < double > ans1;
		ans1 = ans;
		double ans=0, ans2 = 0;
		for (int i = 0;i< numbers.size(); i++) {
			if((i) == 0){
				ans += ((numbers[i]));
			}else{
				ans1[i] += ((numbers[i])*(ans2));
				ans += ans1[i];
				ans2 = ans;
			}	
		}
		return vector < int > (ans);
		//cout << ans << endl;
		/*for(int i=0;i<ans.size();i++)
		 cout<<ans[i]; */
	}
	/*	return empty product
	*/
}
double sum_product2(vector < int > numbers){
vector < double > ans = vector < double > ();
for (int i = 0;i<numbers.size(); i++) {
	if((i) == 0){
		ans[i]=(numbers[i])+ans[i];}else{
		ans[i]=((ans[i-1])*(ans[i]))+(numbers[i]);}}return ans;
}
