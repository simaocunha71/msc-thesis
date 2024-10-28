	if(lst1.size()==lst2.size()){
		for(int i=0;i<lst1.size();i++){
			if(lst1[i]%2==0){
				continue;
			}else if(lst2[i]%2==0){
				lst1[i]=lst2[i];
				continue A;
			}else if(i==lst1.size()-1){
				return "NO";
			}else if(lst2[i+1]%2==0){
				lst1[i]=lst2[i+1];
				continue A;
			}else if(lst2[i+1]%2==1){
				lst1[i]=lst2[i];
				continue A;
			}
		}
	}else{
		if(lst1.size()>lst2.size()){
			return "NO";
		}
	}
	return "YES";
}

int main(){
	vector<int> lst1={1, 2, 3, 4};
	vector<int> lst2={1, 2, 3, 4};
	printf("%s\n",exchange(lst1,lst2).c_str());
	lst1={1, 2, 3, 4};
	lst2={1, 5, 3, 4};
	printf("%s\n",exchange(lst1,lst2).c_str());
	lst1={1, 2, 3, 4};
	lst2={1, 2, 3, 4};
	printf("%s\n",exchange(lst1,lst2).c_str());
	lst1={1, 2, 3, 4};
	lst2={1, 2, 3, 4,5};
	printf("%s\n",exchange(lst1,lst2).c_str());
	lst1={1, 2, 3, 4