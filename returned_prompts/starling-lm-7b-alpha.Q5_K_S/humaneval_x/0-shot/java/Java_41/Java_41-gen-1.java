
    // Here's a solution that's O(n).  It takes advantage of the fact that
    // the cars all move at the same speed.

    int total = 0;

    // The left-to-right cars can only collide with the right-to-left cars that
    // are moving in the opposite direction.  Here, we calculate how far along
    // the road the right-to-left cars are when the left-to-right cars are at
    // position i.  For example, when the left-to-right cars are at position 1,
    // the right-to-left cars are at position 1, 2, 3, ..., 2n.

    int[] rightToLeftPositions = new int[2 * n];
    for (int i = 0; i < 2 * n; i++) {
        rightToLeftPositions[i] = i + 1;
    }

    // Here's the tricky part.  The left-to-right cars can collide with the
    // right-to-left cars that are at positions 2n - i, 2n - i - 1, ..., 2n - i - n + 1.
    // However, we can only collide with one of them, the one that is at position
    // 2n - i - (n - 1).  (We can prove this by induction and the Pigeon-Hole Principle.)
    // As a result, we need to slide the window of right-to-left cars along so that
    // the right-to-left car at position 2n - i - (n - 1) is always at the front.

    int leftToRightPosition = 1;
    for (int i = 0; i < n; i++) {
        int rightToLeftCarAtFrontOfWindow = rightToLeftPositions[2 * n - leftToRightPosition - (n - 1)];
        if (rightToLeftCarAtFrontOfWindow <= leftToRightPosition) {
            total += 1;
        }
        rightToLeftPositions[leftToRightPosition] = rightToLeftPositions[leftToRightPosition + 