	vector<int> res;
	for(int i=0;i<l1.size();i++){
		for(int j=0;j<l2.size();j++){
			if(l1[i]==l2[j])
				res.push_back(l1[i]);
		}
	}
	sort(res.begin(),res.end());
	res.erase(unique(res.begin(),res.end()),res.end());
	return res;
}
int main()
{
	vector<int> l1={1, 4, 3, 34, 653, 2, 5};
	vector<int> l2={5, 7, 1, 5, 9, 653, 121};
	vector<int> res=common(l1,l2);
	for(int i=0;i<res.size();i++){
		printf("%d ",res[i]);
	}
	return 0;
}
