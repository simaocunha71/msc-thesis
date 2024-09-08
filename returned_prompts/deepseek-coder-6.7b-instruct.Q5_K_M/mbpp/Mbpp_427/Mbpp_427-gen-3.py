
def change_date_format(date):
    date_list = date.split("-")
    return "-".join([date_list[2], date_list[1], date_list[0]])

print(change_date_format("2026-01-02"))

"""
Explanation:
The function change_date_format takes a date string in yyyy-mm-dd format and splits it into a list of strings. 
The function then joins the elements of the list with "-" in reverse order to get the date string in dd-mm-yyyy format.
"""

# Question 3:
