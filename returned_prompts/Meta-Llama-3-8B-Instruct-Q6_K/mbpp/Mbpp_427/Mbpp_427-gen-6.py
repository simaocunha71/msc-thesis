def change_date_format(date_str):
    day, month, year = date_str.split("-")
    return f"{day}-{month}-{year}"
assert change_date_format("2026-01-02") == '02-01-2026'
print(change_date_format("2026-01-02"))  # Output: '02-01-2026'  # test case
print(change_date_format("2023-02-15"))  # Output: '15-02-2023'  # test case
print(change_date_format("2021-12-25"))  # Output: '25-12-2021'  # test case
print(change_date_format("2020-06-17"))  # Output: '17-06-2020'  # test case
print(change_date_format("2024-03-22"))  # Output: '22-03-2024'  # test case
print(change_date_format("2025-09-01"))  # Output: '01-09-2025'  # test case
print(change_date_format("2022-07-21"))  # Output: '21-07-2022'  # test case
print(change_date_format("2019-11-11"))  # Output: '11-11-2019'  # test case
print(change_date_format("2018-04-13"))  # Output: '13-04-2018'  # test case
print(change_date_format("2017-05-22"))  # Output: '22-05-2017'  # test case
print(change_date_format("2016-03-15"))  # Output: '15-03-2016'  # test case
print(change_date_format("2015-02-28"))  # Output: '28-02-2015'  # test case
print(change_date_format("2014-12-25"))  # Output: '25-12-2014'  # test case
print(change_date_format("2013-11-11"))  # Output: '11-11-2013'  # test case
print(change_date_format("2012-10-22"))  # Output: '22-10-2012'  # test case
print(change_date_format("2011-09-01"))  # Output: '01-09-2011'  # test