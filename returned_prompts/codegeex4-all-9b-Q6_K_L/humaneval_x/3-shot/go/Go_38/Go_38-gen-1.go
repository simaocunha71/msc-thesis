
I'm not sure you can be asking for any more feedback on this code. It's already pretty clean, and follows the conventions for Go code. I'd be happy to point out some minor tweaks though.

In HasCloseElements, you can use range instead of a manual for loop to iterate over the slice.
The comment in HasCloseElements is a bit out of place. It would be better to put it above the function, or even remove it entirely since the function name already describes what it does.
In HasCloseElements, you could use a single return statement to return the result of the for loop.
In SeparateParenGroups, the comment about ignoring spaces is a bit confusing. It would be better to just say that spaces are ignored.
In SeparateParenGroups, you can use a for range loop to iterate over the string. This will iterate over each rune, which is what you want.
In SeparateParenGroups, you can use the append function to add a rune to a string. This will convert the rune to a string for you, which is what you want.
In SeparateParenGroups, you can use the len function to get the length of a string. This will give you