/*
The logic behind the solution is simple.
We first find the intersection of the two intervals.
If the intersection is empty, we return "NO".
Otherwise, we calculate the length of the intersection.
If the length is a prime number, we return "YES", otherwise, we return "NO".

We have to note that the given intervals are closed, which means that the interval (start, end)
includes both start and end. Therefore, the length of the intersection is the difference between the
larger end and the smaller start of the two intervals.
*/

string intersection( vector<int> interval1,vector<int> interval2){
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if (start > end) return "NO";
    int len = end - start + 1;
    if (len == 1 || len == 2) return "NO";
    for (int i = 2; i < len; i++) {
        if (len % i == 0) return "NO";
    }
    return "YES";
}

B:
/*
The problem is solved by first finding the intersection of the two intervals.
If the intersection is empty, we return "NO".
Otherwise, we calculate the length of the intersection.
If the length is a prime number, we return "YES", otherwise, we return "NO".

The intersection of the two intervals is the interval that contains the maximum of the two
start points and the minimum of the two end points.

The length of the intersection is the difference between the larger end and the smaller start of the two intervals.
*/

string intersection( vector<int> interval1,vector<int> interval2){
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if (start > end) return "NO";
    int len = end - start + 1;
    if (len == 1 || len == 2) return "NO";
    for (int i = 2; i < len; i++) {
        if (len % i == 0) return "NO";
    }
    return "YES";
}

C:
/*
The problem is solved by first finding the intersection of the two intervals.
If the intersection is empty, we return "NO".
Otherwise, we calculate the length of the intersection.
If the length is a prime number, we return "