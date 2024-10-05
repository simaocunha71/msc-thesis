	string result;
	for(int i=0;i<strings.size();i++)
		result+=strings[i];
	return result;
}





/*
Square root of a number
>>> square_root(144)
12
>>> square_root(4)
2
>>> square_root(2)
1
>>> square_root(-1)
-1
>>> square_root(0)
0
>>> square_root(-0)
0
*/
#include<cmath>
int square_root(int number){
	if(number<0)return -square_root(-number);
	return (int)sqrt(number);
}




/*
Check if a number is prime
>>> is_prime(2)
True
>>> is_prime(3)
True
>>> is_prime(4)
False
>>> is_prime(5)
True
>>> is_prime(6)
False
>>> is_prime(7)
True
>>> is_prime(8)
False
>>> is_prime(9)
False
>>> is_prime(10)
False
>>> is_prime(11)
True
>>> is_prime(12)
False
>>> is_prime(13)
True
>>> is_prime(14)
False
>>> is_prime(15)
False
>>> is_prime(16)
False
>>> is_prime(17)
True
>>> is_prime(18)
False
>>> is_prime(19)
True
>>> is_prime(20)
False
>>> is_prime(21)
False
>>> is_prime(22)
False
>>> is_prime(23)
True
>>> is_prime(24)
False
>>> is_prime(25)
False
>>> is_prime(26)
False
>>> is_prime(27)
False
>>> is_prime(28)
False
>>> is_prime(29)
True
>>> is_prime(30)
False
>>> is_prime(31)
True
>>> is_prime(32)
False
>>> is_prime