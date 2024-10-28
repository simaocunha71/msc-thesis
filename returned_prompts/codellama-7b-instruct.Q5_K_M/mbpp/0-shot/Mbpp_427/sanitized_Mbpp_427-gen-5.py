def change_date_format(date_str):
    # Split the date string into its parts
    date_parts = date_str.split("-")
    # Reverse the order of the parts
    date_parts.reverse()
    # Join the parts back into a string
    return "-".join(date_parts)