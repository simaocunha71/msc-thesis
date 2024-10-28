
    import re

    def file_name_check(file_name):
        if (re.match(r'^[A-Za-z][A-Za-z0-9]{0,2}\.([Tt][Xx][Tt])|([Ee][Xx][Ee])|([Dd][Ll][Ll])$', file_name)):
            return 'Yes'
        else:
            return 'No'

    print(file_name_check("example.txt"))  # 应该返回 "Yes"
    print(file_name_check("1example.dll"))  # 应该返回 "No"
    print(file_name_check("example.pdf"))  # 应该返回 "No"
    print(file_name_check("example"))  # 应该返回 "No"
    print(file_name_check("ex.ample.txt"))  # 应该返回 "No"
    print(file_name_check("exam_ple.txt"))  # 应该返回 "No"
    print(file_name_check("example.exe"))  # 应该返回 "Yes"
    print(file_name_check("ExAmPlE.tXt"))  # 应该返回 "Yes"
    print(file_name_check("ExAmPlE9.tXt"))  # 应该返回 "Yes"
    print(file_name_check("ExAmPlE99.tXt"))  # 应该返回 "No" （超过2个数字）
    print(file_name_check("ExAmPlE.pdf"))  # 应该返回 "No" （不支持的文件类型）

    该函数使用正则表达式来检查文件名是否符合要求。正则表达式的结构如下：
    - ^[A-Za-z] 以字母开头
    - [A-Za-z0-9]{0,2} 可选地包含最多两个字母数字字符
    - \. 包含一个点
    - ([Tt][Xx][Tt]|[Ee][Xx