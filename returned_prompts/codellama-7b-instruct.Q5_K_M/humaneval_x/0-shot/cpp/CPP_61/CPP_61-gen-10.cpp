	int left_index = 0;
	int right_index = 0;
	for(int i = 0; i < brackets.length(); i++){
		if(brackets[i] == '('){
			left_index = i;
			break;
		}
	}
	for(int j = brackets.length() - 1; j >= 0; j--){
		if(brackets[j] == ')'){
			right_index = j;
			break;
		}
	}
	if(left_index <= right_index){
		if(left_index == right_index){
			brackets.erase(left_index, 1);
			brackets.erase(right_index, 1);
			goto A;
		}
		return false;
	}
	return true;
}
int main(){
	string brackets = "()";
	printf("%d\n", correct_bracketing(brackets));
	return 0;
}
