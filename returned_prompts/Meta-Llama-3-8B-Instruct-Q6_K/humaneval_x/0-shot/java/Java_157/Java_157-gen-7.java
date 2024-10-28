        // Sort the sides to ensure that a <= b <= c
        int[] sides = {a, b, c};
        Arrays.sort(sides);

        // A right-angled triangle has one side that is the hypotenuse (the longest
        // side), one side that is the opposite (the side opposite the right angle),
        // and one side that is the adjacent (the side next to the right angle).
        // The hypotenuse must be the longest side (c), and the opposite side must
        // be the shorter of the other two sides (a or b).
        // The adjacent side must be the remaining side (the other of a or b).
        // If a^2 + b^2 = c^2, then the triangle is a right-angled triangle.
        return (sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2]);
    }

