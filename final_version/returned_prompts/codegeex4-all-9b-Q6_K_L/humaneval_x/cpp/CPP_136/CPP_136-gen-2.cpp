#include <vector>
using namespace std;

vector<int> largest_smallest_integers(vector<int> lst) {
    int smallest = 0;
    int largest = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (lst[i] < 0) {
            if (lst[i] > largest) {
                largest = lst[i];
            }
        }
        else if (lst[i] > 0) {
            if (lst[i] < smallest) {
                smallest = lst[i];
            }
        }
    }
    return {largest, smallest};
}

