	if(array.empty())return array;
	int sum = array[0]+array.back();
	if(sum%2==0){
		sort(array.begin(),array.end(),greater<int>());
	}else{
		sort(array.begin(),array.end());
	}
	return array;
}
int main(){
	vector<int> array={2, 4, 3, 0, 1, 5};
	vector<int> array2={2, 4, 3, 0, 1, 5, 6};
	printf("%s\n",sort_array(array).empty()?"{}":"{");
	printf("%d, ",array[0]);
	for(int i=1;i<array.size();i++)printf("%d, ",array[i]);
	printf("%s\n",sort_array(array).empty()?"{}":"}");
	printf("%s\n",sort_array(array2).empty()?"{}":"{");
	printf("%d, ",array2[0]);
	for(int i=1;i<array2.size();i++)printf("%d, ",array2[i]);
	printf("%s\n",sort_array(array2).empty()?"{}":"}");
	return 0;
}










































































































































































































