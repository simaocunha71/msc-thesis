#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
using namespace std;

double mean_absolute_deviation(vector<double> numbers) {
    double mean = accumulate(numbers.begin(), numbers.end(), 0.0) / numbers.size();
    double sum = 0.0;
    for (double number : numbers) {
        sum += fabs(number - mean);
    }
    return sum / numbers.size();
}

int main() {
    vector<double> numbers = {1.0, 2.0, 3.0, 4.0};
    double mad = mean_absolute_deviation(numbers);
    cout << "Mean Absolute Deviation: " << mad << endl;
    return 0;
}

B:
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

double mean_absolute_deviation(vector<double> numbers) {
    double sum = 0.0;
    for (double number : numbers) {
        sum += fabs(number - numbers[0]);
    }
    return sum / numbers.size();
}

int main() {
    vector<double> numbers = {1.0, 2.0, 3.0, 4.0};
    double mad = mean_absolute_deviation(numbers);
    cout << "Mean Absolute Deviation: " << mad << endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
using namespace std;

double mean_absolute_deviation(vector<double> numbers) {
    double sum = 0.0;
    double mean = accumulate(numbers.begin(), numbers.end(), 0.0) / numbers.size();
    for (double number : numbers) {
        sum += fabs(number - mean);
    }
    return sum / numbers.size();
}

int main() {
    vector<double> numbers = {1.0, 2.0, 3.0, 4.0};
    double mad = mean_absolute_deviation(numbers);
    cout << "Mean Absolute Deviation: " << mad << endl;
    return 0;
}

D:
#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
using namespace std;

double mean_absolute_deviation(vector<double> numbers) {
    double mean = accumulate(numbers.begin(), numbers.end(), 0.0) / numbers.size();
    double sum = 0.0;
    for (double number : numbers) {
        sum += abs(number - mean);
    }
    return sum / numbers