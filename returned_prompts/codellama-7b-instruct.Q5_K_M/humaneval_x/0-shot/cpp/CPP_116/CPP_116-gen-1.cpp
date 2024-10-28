	vector<int> sorted;
	for(int i=0; i<arr.size(); i++)
		sorted.push_back(arr[i]);
	sort(sorted.begin(), sorted.end());
	return sorted;
}
void main()
{
	vector<int> arr={1, 5, 2, 3, 4};
	vector<int> sorted=sort_array(arr);
	for(int i=0; i<sorted.size(); i++)
		printf("%d ", sorted[i]);
}


