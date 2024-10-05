	int sum=0,l=q.size();
	for(int i=0;i<l;i++)sum+=q[i];
	if(sum>w)return false;
	for(int i=0,j=l-1;i<l/2&&j>=l/2;i++,j--)
		if(q[i]!=q[j])return false;
	return true;
}
int main(){
	vector<int> a={1,2};
	printf("%d",will_it_fly(a,5));
}








*/

																																																																																																																																																																																																																																																																																																																																																																														