def change_date_format(date):
    # Splitting the date into year, month and day
    year, month, day = date.split("-")
    
    # Returning the date in dd-mm-yyyy format
    return f'{day}-{month}-{year}'