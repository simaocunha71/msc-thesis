    int m, d, y, days;
    sscanf(date.c_str(), "%d-%d-%d", &m, &d, &y);
    if(m<1 || m>12 || d<1 || d>31 || y<1 || y>9999)
        return false;
    if(m==2){
        if(y%4==0 && (y%100!=0 || y%400==0))
            days = 29;
        else
            days = 28;
    }
    else if(m==4 || m==6 || m==9 || m==11)
        days = 30;
    else
        days = 31;
    if(d>days)
        return false;
    return true;
}
int main(){
    printf("%d\n",valid_date("03-11-2000"));
    printf("%d\n",valid_date("15-01-2012"));
    printf("%d\n",valid_date("04-0-2040"));
    printf("%d\n",valid_date("06-04-2020"));
    printf("%d\n",valid_date("06/04/2020"));
    return 0;
}
 
C:
#include <stdio.h>
#include <string.h>

int main() {
    printf("%d\n", valid_date("03-11-2000")); // 1
    printf("%d\n", valid_date("15-01-2012")); // 0
    printf("%d\n", valid_date("04-0-2040")); // 0
    printf("%d\n", valid_date("06-04-2020")); // 1
    printf("%d\n", valid_date("06/04/2020")); // 0
    return 0;
}

bool valid_date(char *date) {
    char mm[3], dd[3], yyyy[5];
    sscanf(date, "%s-%s-%s", mm, dd, yyyy);
    int m, d, y;
    m = atoi(mm);
    d = atoi(dd);
    y = atoi(yyyy);
    if (m < 1 || m > 12 || d < 1 || d > 31 || y < 1 || y > 9999) {
        return false;
    }
    if (m == 2) {
        if (y % 4 == 0 && (y % 100 != 0 || y % 400 == 0))
