        // Sorting the sides
        int[] sides = {a, b, c};
        Arrays.sort(sides);

        // Right angle triangle has sides a^2 + b^2 = c^2
        return Math.pow(sides[0], 2) + Math.pow(sides[1], 2) == Math.pow(sides[2], 2);
    }
}

