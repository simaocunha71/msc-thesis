	int c=0;
	for(int i=0;i<lst1.size();i++){
		if(lst1[i]%2==0){
			continue;
		}
		else{
			for(int j=0;j<lst2.size();j++){
				if(lst2[j]%2==0){
					swap(lst1[i],lst2[j]);
					c++;
					goto A;
				}
			}
		}
	}
	if(c==0){
		return "NO";
	}
	else{
		return "YES";
	}
}

int main(){
	vector<int> lst1={1,2,3,4};
	vector<int> lst2={1,2,3,4};
	printf("%s\n",exchange(lst1,lst2).c_str());
	return 0;
}

*/



































































































































































































































































