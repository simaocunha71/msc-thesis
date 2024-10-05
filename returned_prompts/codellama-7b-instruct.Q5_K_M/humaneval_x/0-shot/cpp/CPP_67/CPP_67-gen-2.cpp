	return n - (s.find("apples") != string::npos ? atoi(s.substr(s.find("apples") + 7).c_str()) : 0) - (s.find("oranges") != string::npos ? atoi(s.substr(s.find("oranges") + 7).c_str()) : 0);
}


