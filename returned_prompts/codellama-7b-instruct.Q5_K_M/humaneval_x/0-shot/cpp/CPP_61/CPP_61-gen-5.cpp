if (brackets.length() == 0) return true;
if (brackets[0] == ')') return false;
if (brackets[0] == '('){
	brackets = brackets.substr(1, brackets.length() - 1);
	goto A;
}
return false;
