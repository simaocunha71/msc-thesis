
Your solution is correct, but you can make it more efficient by breaking the loop as soon as you find the smallest even number (this way you will not need to iterate over the whole list). Here is how you can do it:
public List<Integer> pluck(List<Integer> arr) {

    int smallest_value = Integer.MAX_VALUE;
    int index = -1;

    for (int i = 0; i < arr.size(); i++) {
        int current_value = arr.get(i);
        if (current_value % 2 == 0 && current_value < smallest_value) {
            smallest_value = current_value;
            index = i;
            break; // Break the loop as soon as you find the smallest even number
        }
    }

    if (index == -1) return Collections.emptyList();
    else return Arrays.asList(smallest_value, index);
}

This will make your solution more efficient, especially for large lists.