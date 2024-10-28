    if (n>m)
    return "-1";
    int sum=0;
    for (int i=n;i<=m;i++)
    {
        sum+=i;
    }
    float avg=(float)sum/(m-n+1);
    int rounded_avg=round(avg);
    string binary;
    while (rounded_avg>0)
    {
        if (rounded_avg%2==1)
        {
            binary.insert(0,"1");
        }
        else
        {
            binary.insert(0,"0");
        }
        rounded_avg/=2;
    }
    while (binary.length()<4)
    {
        binary.insert(0,"0");
    }
    return binary;
}
// This solution works, but it's not efficient for large inputs because it
// uses string concatenation, which has a time complexity of O(n).  A
// more efficient solution would use a stringstream instead of a string,
// and would calculate the binary representation in one step.  Here's an
// example of how to do that:
#include <sstream>
string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }
    int sum = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
    }
    float avg = (float)sum / (m - n + 1);
    int rounded_avg = round(avg);
    stringstream ss;
    ss << hex << rounded_avg;
    return ss.str();
}
// This solution is more efficient because it uses a stringstream to
// calculate the binary representation in one step, rather than
// concatenating strings.  It also uses the 'hex' manipulator to
// convert the integer to binary, which is more efficient than
// manually calculating the binary representation.  However, it still
// has a time complexity of O(n) because it needs to calculate the sum
// of the integers.  A more efficient solution would be to use a
// different algorithm that doesn't require calculating the sum of the
// integers.  For example, you could use a formula to calculate the
// average directly, without needing to sum the integers.  Here's an
// example of how to do that:
string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }
    float avg = (float)(m + n) / 2;
    int rounded_avg