	if(n==1) return 2;
	if(n==2) return 3;
	if(n==3) return 5;
	int a,b,c,i;
	a=0;
	b=1;
	c=1;
	while(c<n){
		c=a+b;
		a=b;
		b=c;
		if(c%2==0) continue A;
		for(i=3;i<=c/2;i++) if(c%i==0) continue A;
		return c;
	}
	return -1;
}





/*
Given an array of ints, return the sum of the elements. The sum includes all the ints in the array,
so the array can be empty or can have one or more ints in it.

sum_array([1, 2, 3]) → 6
sum_array([1, 2, 3, 4]) → 10
sum_array([]) → 0


*/























































/*
Given three ints, a, b, and k, return the sum of the three
numbers if and only if a > b and a > k, or b > k and b > a,
or k > a and k > b. In other words, whichever of the three
numbers is the largest is the one that "wins". Note that a and b
can be the same size, or a and b can be the same value.

big_sum(1, 2, 3) → 6
big_sum(1, 3, 2) → 6
big_sum(3, 2, 1) → 6

*/














































