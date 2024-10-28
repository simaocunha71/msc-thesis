if(a.type()==typeid(int)&&b.type()==typeid(int)){
	if(a<b)
		return b;
	else
		return a;
}
else if(a.type()==typeid(float)&&b.type()==typeid(float)){
	if(a<b)
		return b;
	else
		return a;
}
else if(a.type()==typeid(string)&&b.type()==typeid(string)){
	string s1,s2;
	s1=(string)a;
	s2=(string)b;
	if(s1<s2)
		return s2;
	else if(s1==s2)
		return "None";
	else
		return s1;
}
else if(a.type()==typeid(int)&&b.type()==typeid(string)){
	string s1,s2;
	s1=(string)a;
	s2=(string)b;
	if(s1<s2)
		return s2;
	else if(s1==s2)
		return "None";
	else
		return s1;
}
else if(a.type()==typeid(string)&&b.type()==typeid(float)){
	string s1,s2;
	s1=(string)a;
	s2=(string)b;
	if(s1<s2)
		return s2;
	else if(s1==s2)
		return "None";
	else
		return s1;
}
else if(a.type()==typeid(string)&&b.type()==typeid(string)){
	string s1,s2;
	s1=(string)a;
	s2=(string)b;
	if(s1<s2)
		return s2;
	else if(s1==s2)
		return "None";
	else
		return s1;
}
else if(a.type()==typeid(float)&&b.type