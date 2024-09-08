/*
Return the number of days in a given month.
>>> days_in_month(1)
31
>>> days_in_month(2)
28
>>> days_in_month(2, 2000)
29
>>> days_in_month(2, 1900)
28
>>> days_in_month(3)
31
>>> days_in_month(4)
30
>>> days_in_month(5)
31
>>> days_in_month(6)
30
>>> days_in_month(7)
31
>>> days_in_month(8)
31
>>> days_in_month(9)
30
>>> days_in_month(10)
31
>>> days_in_month(11)
30
>>> days_in_month(12)
31
*/
#include<stdio.h>
using namespace std;
int days_in_month(int month, int year){

B:
/*
Return the index of the first occurrence of a given value in a given list, or -1 if it is not present.
>>> find([1, 2, 3], 1)
0
>>> find([1, 2, 3], 3)
2
>>> find([1, 2, 3], 4)
-1
>>> find([1, 2, 3, 1, 2, 3], 1)
0
>>> find([1, 2, 3, 1, 2, 3], 3)
2
>>> find([1, 2, 3, 1, 2, 3], 4)
-1
>>> find([1, 2, 3, 1, 2, 3], 2)
1
>>> find([], 1)
-1
*/
#include<stdio.h>
using namespace std;
int find(list, int val){

C:
/*
Return the number of occurrences of a given value in a given list.
>>> count([1, 2, 3], 1)
1
>>> count([1, 2, 3], 3)
1
>>> count([1, 2, 3], 4)
0
>>> count([1, 2, 3, 1, 2, 3], 1)
2
>>> count([1, 2, 3, 1, 2, 3], 3)
2
>>> count([1, 2, 3, 1, 2, 3], 4)
0
>>> count([1,