    vector<int> result;
    int num_abs = abs(num);
    while(num_abs > 0){
        int digit = num_abs % 10;
        if(digit % 2 == 0){
            result.push_back(1);
        }
        else{
            result.push_back(0);
        }
        num_abs /= 10;
    }
    return result;
}

int main(){
    int num;
    scanf("%d", &num);
    vector<int> result = even_odd_count(num);
    int even = 0, odd = 0;
    for(int i = 0; i < result.size(); i++){
        if(result[i] == 0){
            odd++;
        }
        else{
            even++;
        }
    }
    printf("{");
    printf("%d,%d}", even, odd);
    printf("}\n");
    return 0;
}

*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> even_odd_count(int num) {
    vector<int> result;
    while (num > 0) {
        result.push_back(num % 2);
        num /= 10;
    }
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    int num;
    cin >> num;
    vector<int> result = even_odd_count(num);
    int even_count = count(result.begin(), result.end(), 0);
    int odd_count = count(result.begin(), result.end(), 1);
    cout << "{" << even_count << "," << odd_count << "}" << endl;
    return 0;
}





























































