	if (l.empty()) return true;
	if (l.front() < t) {
		l.erase(l.begin());
		goto A;
	}
	return false;
}

