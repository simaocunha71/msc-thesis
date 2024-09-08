def change_date_format(date):
    date_parts = date.split("-")
    return "{}-{}-{}".format(date_parts[2], date_parts[1], date_parts[0])

print(change_date_format("2026-01-02"))

