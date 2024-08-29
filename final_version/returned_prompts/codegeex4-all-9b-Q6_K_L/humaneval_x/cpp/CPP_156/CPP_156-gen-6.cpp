//def int_to_mini_roman(number):
		#result = ''
		#roman_map = {1000:'m', 900:'cm', 500:'d', 400:'cd', 100:'c', 90:'xc', 50:'l', 40:'xl', 10:'x', 9:'ix', 5:'v', 4:'iv', 1:'i'}
		#for k,v in roman_map.items():
			#if number >= k:
				#result += v
				#number -= k
		#return result
		#return ''.join([roman_map[k] for k in sorted(roman_map) if k <= number])


B:
def int_to_mini_roman(number):
		roman_map = {1000:'m', 900:'cm', 500:'d', 400:'cd', 100:'c', 90:'xc', 50:'l', 40:'xl', 10:'x', 9:'ix', 5:'v', 4:'iv', 1:'i'}
		result = ''
		for k,v in roman_map.items():
			while number >= k:
				result += v
				number -= k
		return result

