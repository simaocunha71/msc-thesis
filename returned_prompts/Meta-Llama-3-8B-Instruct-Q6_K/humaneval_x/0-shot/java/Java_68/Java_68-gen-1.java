    public List<Integer> pluck(List<Integer> arr) {
        List<Integer> result = new ArrayList<>();
        if (arr.isEmpty()) {
            return result;
        }
        int minEvenIndex = -1;
        int minValue = Integer.MAX_VALUE;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < minValue) {
                minValue = arr.get(i);
                minEvenIndex = i;
            }
        }
        if (minEvenIndex != -1) {
            result.add(minValue);
            result.add(minEvenIndex);
        }
        return result;
    }

Explanation:
This solution first checks if the input list is empty. If it is, it returns an empty list. 

Then it initializes two variables, `minEvenIndex` and `minValue`, to keep track of the smallest even value and its index. 

It then iterates over the list, checking each value to see if it's even and smaller than the current `minValue`. If it is, it updates `minValue` and `minEvenIndex`.

Finally, it checks if `minEvenIndex` is still -1 (meaning no even values were found). If it's not, it adds `minValue` and `minEvenIndex` to the result list and returns it. If it is, it returns an empty list. 

This solution has a time complexity of O(n), where n is the size of the input list, because it iterates over the list once. It has a space complexity of O(1), because it uses a constant amount of space to store the result and the variables. 