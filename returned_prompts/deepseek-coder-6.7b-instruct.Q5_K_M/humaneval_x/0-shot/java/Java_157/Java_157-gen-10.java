        // create an array from the sides
        int[] sides = {a, b, c};
        // sort the array
        Arrays.sort(sides);

        // return true if the square of the hypotenuse is equal to the sum of the squares of the other two sides
        return Math.pow(sides[2], 2) == Math.pow(sides[0], 2) + Math.pow(sides[1], 2);
    }
}

