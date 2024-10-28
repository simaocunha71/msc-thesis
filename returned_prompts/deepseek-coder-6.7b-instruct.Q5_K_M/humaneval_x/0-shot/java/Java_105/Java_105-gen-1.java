        List<String> names = new ArrayList<>();
        List<Integer> numbers = new ArrayList<>();

        for (int i: arr) {
            if (i>=1 && i<=9) {
                numbers.add(i);
            }
        }

        Collections.sort(numbers);
        Collections.reverse(numbers);

        for (int i: numbers) {
            switch (i) {
                case 1: names.add("One"); break;
                case 2: names.add("Two"); break;
                case 3: names.add("Three"); break;
                case 4: names.add("Four"); break;
                case 5: names.add("Five"); break;
                case 6: names.add("Six"); break;
                case 7: names.add("Seven"); break;
                case 8: names.add("Eight"); break;
                case 9: names.add("Nine"); break;
            }
        }

        return names;
    }
}

This solution first filters out the numbers from the array that are not between 1 and 9 inclusive. It then sorts the numbers in ascending order and reverses the order, creating a new array where the numbers are in descending order. Finally, it converts each number in the new array to its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine" and returns the array of these names.

The time complexity of this solution is O(n log n) due to the sorting step, where n is the number of elements in the array. The space complexity is O(n) for the new array that stores the numbers and their corresponding names.

In the worst case scenario, where all elements in the array are between 1 and 9 inclusive, the time complexity of this solution is O(n log n) and the space complexity is O(n).
*/

//M:
/*
