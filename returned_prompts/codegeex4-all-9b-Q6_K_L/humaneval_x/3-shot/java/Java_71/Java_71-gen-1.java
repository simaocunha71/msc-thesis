
You've got a good start on your code.  I don't have time to review all of the questions, but I'll look at the first one and give you some feedback.
Your code has a bug, as it doesn't handle the case when the list is empty.
Also, you're using a for loop with an index variable.  In this case, that's not necessary.  You can use an enhanced for loop which iterates over the elements of the list directly.
Here's my version of your code:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    if (numbers.isEmpty()) {
        return false;
    }

    for (Double number : numbers) {
        for (Double otherNumber : numbers) {
            if (number.equals(otherNumber)) {
                continue;
            }

            double distance = Math.abs(number - otherNumber);
            if (distance < threshold) {
                return true;
            }
        }
    }

    return false;
}

Note that I've also added a check to make sure we don't compare an element to itself.  That's not necessary, but it's a good practice to include such checks.
Also, you can use the equals() method to compare two Double objects.  That's better than using the == operator, because the == operator will only return true if the two variables are the same object, not if they have the same value.
And lastly, I've added some blank lines to make the code easier to read.
I hope that helps!