def move_zero(my_list):
    return [i for i in my_list if i != 0] + [0] * my_list.count(0)


# 1. 순회 및 필터링
# 2. 결과 리턴


# 버블 정렬
def move_zero(my_list):
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] == 0 and my_list[j] != 0:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list


# 2. 순회
# 3. 필터
# 4. 리턴

# 반복문 중첩 혹은 2중 for문을 통해 순회하며 숫자가 0인 경우에 해당 숫자를 0번째로 옮긴다.


# 리스트 컴프리헨션
# 리스트 컴프리헨션을 통해 간결하게 풀 수 있다.
def move_zero(my_list):
    return [i for i in my_list if i != 0] + [0] * my_list.count(0)


# 1. 순회
# 2. 필터
# 3. 리턴

# 반복문 중첩 혹은 2중 for문을 통해 순회하며 숫자가 0인 경우에 해당 숫자