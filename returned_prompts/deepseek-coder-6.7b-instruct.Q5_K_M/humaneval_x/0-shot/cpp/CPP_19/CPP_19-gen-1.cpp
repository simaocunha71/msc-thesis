string words[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
map<string, int> word_to_num;
for(int i=0; i<10; ++i) word_to_num[words[i]] = i;

B:
stringstream ss(numbers);
string word;
vector<string> number_words;
while(ss >> word) number_words.push_back(word);

C:
sort(number_words.begin(), number_words.end(), [&](const string &a, const string &b){
    return word_to_num[a] < word_to_num[b];
});

D:
string sorted_numbers = "";
for(string word : number_words) sorted_numbers += word + " ";
sorted_numbers.pop_back();
return sorted_numbers;
}

int main(){
    string numbers = "three one five";
    cout << sort_numbers(numbers);
    return 0;
}


A: This function uses a map to map strings to their corresponding numbers.
B: The input string is tokenized into individual words.
C: The words are sorted based on their corresponding numbers.
D: The sorted words are recombined into a string.
*/

int main(){
    string numbers = "three one five";
    cout << sort_numbers(numbers);
    return 0;
}

int main() {
    string numbers = "three one five";
    cout << sort_numbers(numbers);
    return 0;
}

int main() {
    string numbers = "three one five";
    cout << sort_numbers(numbers);
    return 0;
}

int main() {
    string numbers = "three one five";
    cout << sort_numbers(numbers);
    return 0;
}

int main() {
    string numbers = "three one five";
    cout << sort_numbers(numbers);
    return 0;
}

int main() {
    string numbers = "