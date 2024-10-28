	int result = 0;
	while(n--){
		if(n != 0)
			goto A;
		
		return result;
	}
}

/*
The question is flawed. Here's why:

In the case where n = 1, the left-to-right car and the right-to-left car
will never collide with each other, since they will always be moving away from
each other.  However, if we take n = 0, the left-to-right car and the right-to-left
car will collide with each other.

It is impossible to have a road that's a perfectly straight infinitely long line.
A line is 1 dimensional and a road is 2 dimensional.  It is impossible to have an
infinite number of cars. 

The function car_race_collision is incorrect because it will always return 0 and
cannot handle the case of n = 0.

The function car_race_collision should have a loop that runs for n + 1 times,
since there are an infinite number of cars and we want to find the first collision.
*/


#include <iostream>
#include <vector>
using namespace std;

int car_race_collision(int n) {
    int result = 0;
    vector<int> left, right;
    left.push_back(1);
    right.push_back(1);
    while (left.size() + right.size() > 0) {
        left.push_back(left.back() + 1);
        right.push_back(right.back() + 1);
        if (left.size() > 0 && right.size() > 0) {
            if (left.back() == right.back()) {
                result++;
            }
        }
    }
    return result;
}

int main() {
    cout << car_race_collision(1) << endl;
    cout << car_race_collision(2) << endl;
    cout << car_race_collision(3) << endl;
    cout << car_race