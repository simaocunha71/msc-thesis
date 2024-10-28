
for _, n := range l {
    if n >= t {
        return false
    }
}

return true

}

*/
package main

import (
	"fmt"
)

func BelowThreshold(l []int, t int) bool {
	for _, n := range l {
		if n >= t {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(BelowThreshold([]int{1, 2, 4, 10}, 100)) // true
	fmt.Println(BelowThreshold([]int{1, 20, 4, 10}, 5))   // false
}
package main

import (
	"fmt"
)

// 1. สร้างฟังก์ชั่นชื่อ "Add" ที่รับค่า a และ b เป็น int และคืนค่าผลบวกของ a และ b
// 2. สร้างฟังก์ชั่นชื่อ "Subtract" ที่รับค่า a และ b เป็น int และคืนค่าผลลบของ a ตามด้วย b
// 3. สร้างฟังก์ชั่นชื่