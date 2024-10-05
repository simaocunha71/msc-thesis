    int i, j, count = 0;
    for(i=0, j=n-1; i<n && j>=0;){
        if(i < j){
            i++;
        }
        else if(i > j){
            j--;
        }
        else{
            i++;
            j--;
        }
        count++;
    }
    return count;
}

int main(){
    int n;
    printf("Enter the number of cars: ");
    scanf("%d", &n);
    printf("Number of collisions: %d\n", car_race_collision(n));
    return 0;
}

Explanation:
This program creates two pointers, i and j. i points to the leftmost car and j points to the rightmost car. It then enters a loop where it increments i if the left car is to the left of the right car, decrements j if the left car is to the right of the right car, and if they are the same, it increments i and decrements j. The count keeps track of the number of collisions.
*/

#include <iostream>
using namespace std;

int car_race_collision(int n) {
    int i = 0, j = n - 1, count = 0;
    while (i <= j) {
        i++;
        j--;
        count++;
    }
    return count;
}

int main() {
    int n;
    cout << "Enter the number of cars: ";
    cin >> n;
    cout << "Number of collisions: " << car_race_collision(n) << endl;
    return 0;
}

Explanation:
This program creates two pointers, i and j. i points to the leftmost car and j points to the rightmost car. It then enters a loop where it increments i and decrements j. The count keeps track of the number of collisions.
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int car_race_collision(int n) {
    vector<