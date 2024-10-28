	vector<int> res;
	for(int i = 0; i < numbers.size(); ++i){
		if(i != 0) res.push_back(delimeter);
		res.push_back(numbers[i]);
	}
	return res;
}
int main(){
	vector<int> numbers;
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; ++i){
		int tmp;
		scanf("%d", &tmp);
		numbers.push_back(tmp);
	}
	int delimeter;
	scanf("%d", &delimeter);
	vector<int> res = intersperse(numbers, delimeter);
	for(int i = 0; i < res.size(); ++i){
		printf("%d", res[i]);
		if(i != res.size() - 1) printf(" ");
	}
	printf("\n");
}




ANSWER:
A

Explanation
The function intersperse takes two parameters: a vector of integers and an integer delimiter. The function creates a new vector that intersperses the input vector numbers with the delimiter.

The function iterates through the input vector and for each element, inserts the delimiter before it in the result vector.

In the main function, the user inputs a vector of integers and a delimiter. The intersperse function is called with these inputs and the result is printed out.



*/


ANSWER:

Explanation
The function intersperse takes two parameters: a vector of integers and an integer delimiter. The function creates a new vector that intersperses the input vector numbers with the delimiter.

The function iterates through the input vector and for each element, inserts the delimiter before it in the result vector.

In the main function, the user inputs a vector of integers and a delimiter. The intersperse function is called with these inputs and the result is printed out.
























