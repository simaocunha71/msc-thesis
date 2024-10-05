}
int main() {
	
	vector<int> q1 = {1, 2};
	vector<int> q2 = {3, 2, 3};
	vector<int> q3 = {3, 2, 3};
	vector<int> q4 = {3};
	
	printf("%d\n",will_it_fly(q1, 5)); // 0
	printf("%d\n",will_it_fly(q2, 1)); // 0
	printf("%d\n",will_it_fly(q2, 9)); // 1
	printf("%d\n",will_it_fly(q4, 5)); // 1

	return 0;
}

S:
#include<stdio.h>
#include<vector>
using namespace std;

bool is_palindrome(vector<int> q){
    int start = 0;
    int end = q.size() - 1;
    while(start < end){
        if(q[start] != q[end])
            return false;
        start++;
        end--;
    }
    return true;
}

bool will_it_fly(vector<int> q,int w){
    int sum = 0;
    for(int i = 0; i < q.size(); i++)
        sum += q[i];
    return is_palindrome(q) && sum <= w;
}

int main() {
	
	vector<int> q1 = {1, 2};
	vector<int> q2 = {3, 2, 3};
	vector<int> q3 = {3, 2, 3};
	vector<int> q4 = {3};
	
	printf("%d\n",will_it_fly(q1, 5)); // 0
	printf("%d\n",will_it_fly(q2, 1)); // 0
	printf("%d\n",will_it_fly(q2, 9)); // 1
	printf("%d\n",will_it_fly(q4, 5)); // 