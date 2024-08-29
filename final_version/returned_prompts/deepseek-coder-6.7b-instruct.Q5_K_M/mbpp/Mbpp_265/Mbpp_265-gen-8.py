def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

print(list_split(['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n'], 3))

# Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

This program works by using a list comprehension with a step of n. The range function is called with a step of n to produce indices into the list lst. For each index i, a slice from i to i+n is taken from lst. The result is a list of lists, where each inner list contains every nth element from lst.
</code>




</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div>



</div