
max := l[0]

for _, value := range l {

	if value > max {

		max = value

	}

}

return max

}

*/

package main

import "fmt"

// Return maximum element in the list.
func MaxElement(l []int) int {
	max := l[0]

	for _, value := range l {
		if value > max {
			max = value
		}
	}

	return max
}

func main() {
	fmt.Println(MaxElement([]int{1, 2, 3}))
	fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
}

// output:
// 3
// 123
// 说明：代码中使用的算法是遍历列表的元素，并将每个元素与当前最大值进行比较。如果当前元素大于当前最大值，则更新当前最大值。最后，返回找到的最大值。
// 这个算法的时间复杂度是O(n)，其中n是列表的长度。
// 这个算法的空间复杂度是O(1)，因为它只需要一个常数量的额外空间来存储最大值。
// 这个算法适用于任何整数列表，无论其长度如何。
// 它应该在计算机科学课程中使用，以帮助学生理解如何在编程问题中使用算法。
// 它也可以用于在实际场景中找到列表中的最大元素。
// 例如，在数据处理、机器学习等领域，需要在数据集中找到最大值以进行进一步的计算。
// 这个算法也可以用于在数据集的不同部分找到最大值，以帮助识别异常值或在某些机器学习算法中找到最有利的特征。
// 总的来说，这个算法是一个基本的算法，但它在各种场景中都非常有用。
// 在实际的编程问题中，可能需要更复杂的算法，但这个算法是一个很好的起点。