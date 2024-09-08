    if(n > m)
        return "-1";
    double sum = 0;
    for(int i = n; i <= m; i++)
        sum += i;
    double avg = sum / (m - n + 1);
    avg = floor(avg + 0.5); // rounded to the nearest integer, smaller one
    string result = "";
    while(avg > 0) {
        if(avg % 2 == 1) result = "1" + result;
        avg = avg / 2;
    }
    if(result.length() == 0) result = "0";
    return result;
}

int main(){
    printf("%s\n",rounded_avg(1, 5).c_str());
    printf("%s\n",rounded_avg(7, 5).c_str());
    printf("%s\n",rounded_avg(10, 20).c_str());
    printf("%s\n",rounded_avg(20, 33).c_str());
    return 0;
}

C:
#include <stdio.h>
#include <math.h>
#include <string.h>

char* rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }
    double sum = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
    }
    double avg = sum / (m - n + 1);
    avg = floor(avg + 0.5);
    char* result = (char*)malloc(32);
    sprintf(result, "%d", (int)avg);
    return result;
}

int main() {
    printf("%s\n", rounded_avg(1, 5));
    printf("%s\n", rounded_avg(7, 5));
    printf("%s\n", rounded_avg(10, 20));
    printf("%s\n", rounded_avg(20, 33));
    return 0;
}
Output:
11
-1
1111
11010
*/



