
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    
    return len(nums) - sum((n if n != 0 and (mod(n-int(n)), mod(-int(n)+1)) == (mod(n+int(n)) - 1) for n in nums))
def main():
	specialFilter([1, 3, 4, 5])
if __name__=="__main__":
    main()