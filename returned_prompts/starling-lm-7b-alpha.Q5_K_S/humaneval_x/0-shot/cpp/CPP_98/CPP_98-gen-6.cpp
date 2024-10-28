	int len = s.size();
	int cnt = 0;
	for(int i = 0; i < len; i += 2){
		if(s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U'){
			cnt++;
		}
	}
	return cnt;
}
int main(){
	string s;
	cin >> s;
	printf("%d\n", count_upper(s));
	return 0;
}

*/











#include<cstdio>
#include<string>
using namespace std;
int count_upper(string s){
	int cnt = 0;
	int len = s.size();
	for(int i = 0; i < len; i += 2){
		if(s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U' && s[i] >= 'A' && s[i] <= 'Z'){
			cnt++;
		}
	}
	return cnt;
}

int main(){
	string s;
	cin >> s;
	printf("%d\n", count_upper(s));
	return 0;
}





































































































































































