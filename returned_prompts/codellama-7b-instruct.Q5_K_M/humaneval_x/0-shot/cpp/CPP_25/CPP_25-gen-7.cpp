	vector<int> ans;
	int n=1;
	for(int i=1;i<=30;i++){
		ans=factorize(i);
		printf("%d:",i);
		for(int j=0;j<ans.size();j++)
			printf(" %d",ans[j]);
		printf("\n");
	}
	return 0;
}
