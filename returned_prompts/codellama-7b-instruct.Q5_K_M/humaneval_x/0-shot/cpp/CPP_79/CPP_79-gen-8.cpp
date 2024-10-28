/*
Write a function called "is_leap_year" that takes in a year as its only parameter.
The function should return true if the year is a leap year. A leap year occurs
every 4 years in our calender. But years that are divisible by 100 are not
considered leap years. However, years that are divisible by 400 are considered leap years.

Examples:
is_leap_year(2019)  // returns false
is_leap_year(2020)  // returns true
is_leap_year(2000)  // returns true
*/
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

bool is_leap_year(int year);

int main(void)
{
    int year;
    do
    {
        year = get_int("Year: ");
    }
    while (year < 0 || year > 9999);

    if (is_leap_year(year))
    {
        printf("%i is a leap year.\n", year);
    }
    else
    {
        printf("%i is not a leap year.\n", year);
    }
}

bool is_leap_year(int year)
{
    if (year % 4 == 0 && year % 100 != 0)
    {
        return true;
    }
    else if (year % 400 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
