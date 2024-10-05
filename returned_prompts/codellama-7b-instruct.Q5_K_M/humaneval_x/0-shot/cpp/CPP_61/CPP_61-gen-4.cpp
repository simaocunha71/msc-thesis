	if(brackets == "") return true;
	if(brackets[0] == ')') return false;
	int i = 1;
	while(brackets[i] != '('){i++;}
	return correct_bracketing(brackets.substr(i+1, brackets.length()-1));
}


