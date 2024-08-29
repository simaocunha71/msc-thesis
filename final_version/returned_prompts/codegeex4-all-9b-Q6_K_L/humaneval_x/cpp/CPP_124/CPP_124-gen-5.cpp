#include <string>
using namespace std;

bool valid_date(string date) {
    // 日期格式验证
    if (date.length() != 10 || date[2] != '-' || date[5] != '-') {
        return false;
    }

    // 分割日期字符串
    string month_str = date.substr(0, 2);
    string day_str = date.substr(3, 2);
    string year_str = date.substr(6, 4);

    // 转换为整数
    int month = stoi(month_str);
    int day = stoi(day_str);
    int year = stoi(year_str);

    // 检查月份范围
    if (month < 1 || month > 12) {
        return false;
    }

    // 检查天数范围
    if ((month == 4 || month == 6 || month == 9 || month == 11) && (day < 1 || day > 30)) {
        return false;
    } else if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && (day < 1 || day > 31)) {
        return false;
    } else if (month == 2) {
        // 检查闰年
        bool is_leap_year = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
        if (is_leap_year && (day < 1 || day > 29)) {
            return false;
        } else if (!is_leap_year && (day < 1 || day > 28)) {
            return false;
        }
    }

    return true;
}

C:
#include <string>
using namespace std;

bool valid_date(string date) {
    // 日期格式验证
    if (date.length() != 10 || date[2] != '-' || date[5] != '-') {
        return false;
    }

    // 分割日期字符串
    string month_str = date.substr(0, 2);
    string day_str = date.substr(3, 2);
    string year_str = date.substr(6, 4);

    // 转换为整数
    int month = stoi(month_str);
    int day = stoi(day_str);
    int year = stoi(year_str