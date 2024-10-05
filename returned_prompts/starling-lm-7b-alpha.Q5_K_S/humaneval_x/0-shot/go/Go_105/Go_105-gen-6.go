
var arr1 = [1, 1, 2, 2, 3, 4, 5, 8]
var arr2 = [8, 5, 4, 3, 2, 2, 1, 1]
var arr3 = [55, 1, -1]

var str1 []string
var str2 []string
var str3 []string

for i := range arr1 {
    switch arr1[i] {
    case 1:
        str1 = append(str1, "One")
    case 2:
        str1 = append(str1, "Two")
    case 3:
        str1 = append(str1, "Three")
    case 4:
        str1 = append(str1, "Four")
    case 5:
        str1 = append(str1, "Five")
    case 6:
        str1 = append(str1, "Six")
    case 7:
        str1 = append(str1, "Seven")
    case 8:
        str1 = append(str1, "Eight")
    case 9:
        str1 = append(str1, "Nine")
    }
}

for i := range arr2 {
    switch arr2[i] {
    case 1:
        str2 = append(str2, "One")
    case 2:
        str2 = append(str2, "Two")
    case 3:
        str2 = append(str2, "Three")
    case 4:
        str2 = append(str2, "Four")
    case 5:
        str2 = append(str2, "Five")
    case 6:
        str2 = append(str2, "Six")
    case 7:
        str2 = append(str2, "Seven")
    case 8:
        str2 = append(str2, "Eight")
    case 9:
        str2 = append(str2, "Nine")
    }
}

for i := range arr3 {
    switch arr3[i] {
   