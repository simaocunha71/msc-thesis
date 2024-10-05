	int len1,len2,i,j;
	len1=l1.size();
	len2=l2.size();
	vector<int> l3;
	for(i=0;i<len1;i++){
		for(j=0;j<len2;j++){
			if(l1[i]==l2[j]){
				if(find(l3.begin(),l3.end(),l1[i])==l3.end())
					l3.push_back(l1[i]);
			}
		}
	}
	sort(l3.begin(),l3.end());
	return l3;
}
int main(){
	vector<int> l1={1, 4, 3, 34, 653, 2, 5};
	vector<int> l2={5, 7, 1, 5, 9, 653, 121};
	vector<int> l3=common(l1,l2);
	for(int i=0;i<l3.size();i++)
		printf("%d, ",l3[i]);
	printf("\n");
}






















































































































































































































