
    Use the following signature:

    vector<int> count_results(const map<string, int>&, const list<int>&)

    For example:

    int main() {
      map<string, int> m;
      m["a"] = 2;
      m["b"] = 3;
      m["c"] = 4;
      list<int> l;
      l.push_back(1);
      l.push_back(2);
      l.push_back(3);
      vector<int> v = count_results(m, l);
      // v[0] = 1
      // v[1] = 2
      // v[2] = 3
      return 0;
    }

    The output should be:

    [1, 2, 3]

    In case of an error, the function should return an empty vector.

    For example:

    int main() {
      map<string, int> m;
      m["a"] = 2;
      m["b"] = 3;
      m["c"] = 4;
      list<int> l;
      l.push_back(1);
      l.push_back(2);
      l.push_back(3);
      vector<int> v = count_results(m, l);
      // v[0] = 1
      // v[1] = 2
      // v[2] = 3
      return 0;
    }

    The output should be:

    [1, 2, 3]

    In case of an error, the function should return an empty vector.

    For example:

    int main() {
      map<string, int> m;
      m["a"] = 2;
      m["b"] = 3;
      m["c"] = 4;
      list<int> l;
      l.push_back(1);
      l.push_back(2);
      l.push_back(3);
      vector<int> v = count_results(m, l);
      // v[0]