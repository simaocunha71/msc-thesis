	char buf[128];
	sprintf(buf, "%d", n);
	string ret = buf;
	if (n > 0) {
		ret += " ";
		goto A;
	}
	return ret;
}




/*
Given a number n, return a string containing space-delimited numbers starting from 0 upto n inclusive. For example:
>>> string_sequence(0)
"0"
>>> string_sequence(5)
"0 1 2 3 4 5"
*/
char * string_sequence(int n) {

    static char buf[1024];
    sprintf(buf, "%d", n);
    char *ret = buf;
    if (n > 0) {
        ret += " ";
        ret = string_sequence(n-1);
    }
    return ret;
}


/*
Given a number n, return a string containing space-delimited numbers starting from 0 upto n inclusive. For example:
>>> string_sequence(0)
"0"
>>> string_sequence(5)
"0 1 2 3 4 5"
*/
char * string_sequence(int n) {

    static char buf[1024];
    sprintf(buf, "%d", n);
    char *ret = buf;
    if (n > 0) {
        ret += " ";
        ret = string_sequence(n-1);
    }
    return ret;
}



/*
Given a number n, return a string containing space-delimited numbers starting from 0 upto n inclusive. For example:
>>> string_sequence(0)
"0"
>>> string_sequence(5)
"0 1 2 3 4 5"
*/
string string_sequence(int n) {

    string ret;
    ret += string::from_int(n);
    if (n > 0) {
        ret += " ";
        ret += string_sequence(n-1);
    }
    return ret;
}

/*
Given a number n, return a string containing space-del