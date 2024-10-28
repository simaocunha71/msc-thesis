
The first two functions look good. The last one has a small bug. It's not checking if the index is even, it's checking if the index is odd. That's why it's always returning 0. Change this line:
if i%2 == 1 && strings.ContainsRune("AEIOU", c) {

to this:
if i%2 == 0 && strings.ContainsRune("AEIOU", c) {

And it should work as expected.