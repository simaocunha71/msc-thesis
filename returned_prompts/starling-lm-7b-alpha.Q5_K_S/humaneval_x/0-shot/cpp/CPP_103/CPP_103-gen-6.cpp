	int num=n+m;
	int cnt=m-n+1;
	if(n>m){
		return "-1";
	}
	if(num/cnt==(num+cnt-1)/cnt){
		return bitset<32>(num/cnt).to_string();
	}else{
		return bitset<32>((num+cnt-1)/cnt).to_string();
	}
}

int main(){
	int n,m;
	while(~scanf("%d%d",&n,&m)){
		printf("%s\n",rounded_avg(n,m).c_str());
	}
	return 0;
}

	   	 		   	  	 				 	  				
```