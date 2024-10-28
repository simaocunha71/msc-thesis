

	if (a.type() != b.type()) {
		return "None";
	}
	if (a.type() == typeid(int)) {
		int x = boost::any_cast<int>(a);
		int y = boost::any_cast<int>(b);
		if (x > y)
			return a;
		else if (x < y)
			return b;
		else
			return "None";
	}
	if (a.type() == typeid(float)) {
		float x = boost::any_cast<float>(a);
		float y = boost::any_cast<float>(b);
		if (x > y)
			return a;
		else if (x < y)
			return b;
		else
			return "None";
	}
	if (a.type() == typeid(string)) {
		string x = boost::any_cast<string>(a);
		string y = boost::any_cast<string>(b);
		if (x > y)
			return a;
		else if (x < y)
			return b;
		else
			return "None";
	}
	return "None";
}
int main() {
	boost::any a = compare_one(1, 2.5);
	cout << a << endl;
	boost::any b = compare_one(1, "2,3");
	cout << b << endl;
	boost::any c = compare_one("5,1", "6");
	cout << c << endl;
	boost::any d = compare_one("1", 1);
	cout << d << endl;
	return 0;
}
