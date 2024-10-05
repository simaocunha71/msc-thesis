
OddCount(["1234567"])

// 返回：["the number of odd elements 4n the str4ng 4 of the 4nput."]

OddCount(["3","11111111"])

// 返回：["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]

在函数OddCount中，我们初始化一个空的切片result来存储输出结果。对于输入切片中的每个字符串v，我们遍历v中的每个字符。如果字符是奇数（通过将字符转换为整数，然后对2取余来确定），我们增加计数。在处理完v中的所有字符后，我们使用fmt.Sprintf创建一个字符串，将计数替换为适当的占位符，并将其附加到result中。然后，我们重置计数并继续处理下一个字符串。最后，我们返回result。

在示例中：

- OddCount(["1234567"])返回["the number of odd elements 4n the str4ng 4 of the 4nput."]，因为字符串"1234567"中有4个奇数数字（1、3、5、7）。

- OddCount(["3","11111111"])返回["the number of odd elements 1n the str1ng 1 of the 