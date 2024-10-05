	for(int i = 0; i < l.size(); i++) {
		for(int j = i+1; j < l.size(); j++) {
			if(l[i]+l[j] == 0) {
				return true;
			}
		}
	}
	return false;
}





/*
The above function can be modified to return the first pair of elements
that sum to zero. If no such pair exists, return -1.
>>> pairs_sum_to_zero({1, 3, -2, 1})
(0, 1)
>>> pairs_sum_to_zero({2, 4, -5, 3, 5, 7})
(3, 5)
>>> pairs_sum_to_zero({1})
-1
*/

pair<int, int> pairs_sum_to_zero(vector<int> l) {
	for (int i = 0; i < l.size(); i++) {
		for (int j = i + 1; j < l.size(); j++) {
			if (l[i] + l[j] == 0) {
				return make_pair(i, j);
			}
		}
	}
	return make_pair(-1, -1);
}










/*
The above function can be modified to return all pairs of elements
that sum to zero, as a vector of pairs. If no such pair exists, return an
empty vector.
>>> pairs_sum_to_zero({1, 3, -2, 1})
[(0, 1)]
>>> pairs_sum_to_zero({2, 4, -5, 3, 5, 7})
[(3, 5), (4, 2)]
>>> pairs_sum_to_zero({1})
[]
*/

vector<pair<int, int>> pairs_sum_to_zero(vector<int> l) {
	vector<pair<int, int>> res;
	for (int i = 0; i < l.size(); i