    public List<Double> findClosestElements(List<Double> numbers) {
        // Find the smallest and largest numbers in the list
        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        // Initialize the closest pair
        double closest = Double.MAX_VALUE;
        List<Double> closestPair = new ArrayList<>();

        // Iterate over the list to find the closest pair
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                if (Math.abs(numbers.get(i) - numbers.get(j)) < closest) {
                    closest = Math.abs(numbers.get(i) - numbers.get(j));
                    closestPair.clear();
                    closestPair.add(numbers.get(i));
                    closestPair.add(numbers.get(j));
                }
            }
        }

        // Sort the closest pair
        closestPair.sort((a, b) -> a.compareTo(b));

        return closestPair;
    }A


C:
    public List<Double> findClosestElements(List<Double> numbers) {
        // Sort the list
        numbers.sort((a, b) -> a.compareTo(b));

        // Initialize the closest pair
        double closest = Double.MAX_VALUE;
        List<Double> closestPair = new ArrayList<>();

        // Iterate over the list to find the closest pair
        for (int i = 0; i < numbers.size() - 1; i++) {
            double diff = numbers.get(i + 1) - numbers.get(i);
            if (diff < closest) {
                closest = diff;
                closestPair.clear();
                closestPair.add(numbers.get(i));
                closestPair.add(numbers.get(i + 1));
            }
        }

        return closestPair;
    }C


R:
    def findClosestElements(nums):
        nums.sort()
        closest = float('inf')
        closest_pair = []
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff < closest:
                closest = diff
                closest_pair = [nums[i], nums[i + 1]]
        return closest_pair

    # Test the function
    print(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: [2.0, 2.2]
    print(findClosestElements([1.0