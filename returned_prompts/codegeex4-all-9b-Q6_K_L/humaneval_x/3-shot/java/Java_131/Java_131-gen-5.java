
The first and last questions are very similar. I'll answer the first and then suggest a modification to the second.
Question 1: hasCloseElements

The method name hasCloseElements is not very descriptive of what the method does. It's not immediately clear what "close" means.
The method doesn't make use of the List interface. It would be better to use this interface directly rather than the concrete implementation ArrayList.
The method is public, but it doesn't make sense to call this method from outside the class. It would be better to make this method private.
The method is not overloaded. If it were, it would be good to have a version that accepts an array rather than a List.

Question 2: separateParenGroups

The method name separateParenGroups is also not very descriptive. It's not immediately clear what "separate groups" means.
The method is public, but it doesn't make sense to call this method from outside the class. It would be better to make this method private.
The method is not overloaded. If it were, it would be good to have a version that accepts a String[] rather than a String.
The method doesn't make use of the StringBuilder class. It would be better to use this class directly rather than the concrete implementation StringBuilder.
The method doesn't make use of the Character class. It would be better to use this class directly rather than the concrete implementation Character.
The method doesn't make use of the toCharArray method. It would be better to use this method directly rather than the concrete implementation toCharArray.
The method doesn't make use of the append method. It would be better to use this method directly rather than the concrete implementation append.
The method doesn't make use of the setLength method. It would be better to use this method directly rather than the concrete implementation setLength.
The method doesn't make use of the ArrayList class. It would be better to use this class directly rather than the concrete implementation ArrayList.
The method doesn't make use of the toString method. It would be better to use this method directly rather than the concrete implementation toString.
The method doesn't make use