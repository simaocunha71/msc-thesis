"""
def change_date_format(date: str) -> str:
    date_parts = date.split('-')
    return f'{date_parts[2]}-{date_parts[1]}-{date_parts[0]}'

assert change_date_format("2026-01-02") == '02-01-2026'
"""

