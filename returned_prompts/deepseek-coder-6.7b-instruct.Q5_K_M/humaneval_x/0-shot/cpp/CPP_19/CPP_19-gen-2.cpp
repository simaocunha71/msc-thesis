    map<string, int> m;
    m["zero"] = 0;
    m["one"] = 1;
    m["two"] = 2;
    m["three"] = 3;
    m["four"] = 4;
    m["five"] = 5;
    m["six"] = 6;
    m["seven"] = 7;
    m["eight"] = 8;
    m["nine"] = 9;

    stringstream ss(numbers);
    string word;
    vector<string> words;
    while (ss >> word) {
        words.push_back(word);
    }

    sort(words.begin(), words.end(), [&m](string &a, string &b) {
        return m[a] < m[b];
    });

    string sorted_numbers = "";
    for (string &word : words) {
        sorted_numbers += word + " ";
    }

    return sorted_numbers.substr(0, sorted_numbers.size() - 1);
}

*/
int main()
{
    string numbers = "three one five";
    cout << sort_numbers(numbers) << endl;
    return 0;
}
```

**Explanation:**

The program uses a map to store the corresponding numbers (as string and integer) to the numbers from "zero" to "nine". The program takes a string of numberals from "zero" to "nine", splits the string into words and sorts them using the map to sort them in ascending order. Then it concatenates the sorted words back into a string and returns it.

**Output:**

```
one three five
```

**Note:** This code only works in C++11 or later as it uses features of C++11 like `std::map`, `std::sort` and `std::stringstream`. If you are using a version of C++ before C++11, you will have to replace these features with their equivalent in older versions of C++.


**Complexity Analysis:**

The time complexity is O(nlogn) because of the sorting operation which takes O(nlogn