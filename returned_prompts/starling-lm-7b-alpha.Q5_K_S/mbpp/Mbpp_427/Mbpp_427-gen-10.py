```
def change_date_format(date):
    year, month, day = date.split("-")
    return "%s-%s-%s" % (day, month, year)
```

Explanation:

The function `change_date_format` takes a date string in the format "yyyy-mm-dd" and splits it into three parts: the year, the month, and the day. It then returns a new string in the format "dd-mm-yyyy" by using string formatting to insert the day, month, and year into the correct positions.

The assert statement tests the function by passing in the date "2026-01-02" and checking if the returned value is "02-01-2026".

Overall, this solution uses string splitting and formatting to convert a date from one format to another.

```python
def change_date_format(date):
    year, month, day = date.split("-")
    return "%s-%s-%s" % (day, month, year)
```
This code defines a function called `change_date_format` that takes a string `date` as input. Inside the function, the `split` method is used to split the `date` string into three parts: `year`, `month`, and `day`, based on the delimiter "-". Then, the `return` statement uses string formatting to create a new string in the format "dd-mm-yyyy" by inserting the `day`, `month`, and `year` variables into the correct positions.

The assert statement is a way to check if a condition is true. In this case, it is checking if the `change_date_format` function returns the correct value when given the input "2026-01-02". If the condition is true, the assert statement passes and the code continues to execute. If the condition is false, an error is raised, indicating that there is a bug in the code.

In summary, this solution uses string manipulation and formatting to convert a date from one format to another, and the assert statement is used to test the correctness of the function.

```python
def change_date_format(date):
    year, month, day = date