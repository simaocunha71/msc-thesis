if(interval1[0]>interval2[1] || interval2[0]>interval1[1]) {
	return "NO";
}

B:
else if(interval1[1]-interval2[0]==1 && interval1[0]-interval2[1]==1) {
	return "YES";
}

C:
else if(interval1[1]-interval2[0]==0 || interval1[0]-interval2[1]==0) {
	return "NO";
}

D:
else {
	return "YES";
}

}

#include <iostream>
#include <vector>
#include <string>
using namespace std;
string intersection(vector<int> interval1, vector<int> interval2) {
    vector<int> temp;
    int i = 0, j = 0;
    if (interval1[0] > interval2[1] || interval2[0] > interval1[1]) {
        return "NO";
    }
    temp.push_back(max(interval1[0], interval2[0]));
    temp.push_back(min(interval1[1], interval2[1]));
    if (temp[1] - temp[0] == 1 && temp[0] - temp[1] == 1) {
        return "YES";
    }
    if (temp[1] - temp[0] == 0 || temp[0] - temp[1] == 0) {
        return "NO";
    }
    return "YES";
}
