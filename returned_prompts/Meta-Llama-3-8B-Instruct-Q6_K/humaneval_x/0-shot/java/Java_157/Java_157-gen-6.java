// a, b, and c are the lengths of the three sides of a triangle.
// A right-angled triangle is a triangle in which one angle is right angle or 90 degree.
// A triangle with sides a, b, and c is right-angled if and only if a^2 + b^2 = c^2.
// This is known as the Pythagorean theorem.

// First, sort the sides in ascending order.
// This is because the side which is equal to c^2 - a^2 - b^2 is the hypotenuse.
Arrays.sort(new int[]{a, b, c});

// Check if a^2 + b^2 = c^2.
return (a*a + b*b) == (c*c);

}

