"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""
from typing import Optional

def extract_nth_element(tuples:list[tuple],n:Optional[int]) -> list[str]:
	if n == None : return tuples
	else if len(tuples) < n : return []
	return [x for i,y in enumerate(tuples[:n-1]) : (x,i,y)]
