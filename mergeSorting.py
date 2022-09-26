def insertion_sorting(l):
    for j in range(1, len(l)):  # 처음 것을 제외하고 삽입함

        key = l[j]
        i = j - 1  # key 값보다 하나 작은 것으로 설정함
        while i >= 0 and l[i] > key:  # key 값보다 클때 까지 그리고 0보다 크거나 같을 때 까지로 설정해야합니다.
            l[i + 1] = l[i]  # 옆으로 옮겨버림
            i = i - 1
        l[i + 1] = key  # 마지막에 존건문을 만족한다면 옆으로 옮겨버린다.


alist = [4, 2, 5, 12, 3, 14, 51, 23, 1234, 1, 23]
insertion_sorting(alist)
print(alist)

sorted = [None]*(20)


def merge(array, left, mid, right):
    global sorted
    Lindex = left
    Rindex = mid + 1
    newIndex = left

    while Lindex <= mid and Rindex <= right:

        if array[Lindex] < array[Rindex]:
            sorted[newIndex] = array[Lindex]
            Lindex += 1
            newIndex += 1
        else:
            sorted[newIndex] = array[Rindex]
            Rindex += 1
            newIndex += 1
    if Lindex > mid:
        sorted[newIndex:newIndex + right - Rindex + 1] = array[Rindex:right + 1]
    else:
        sorted[newIndex: newIndex + left - Lindex + 1] = array[Lindex:mid + 1]
    array[left:right + 1] = sorted[left:right + 1]


count = 0


def merge_sort(array, left, right):
    global count
    count += 1
    if left < right:
        mid = (right + left) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)


list_a = [12, 32, 4, 5, 23, 46, 4, 6, 7, 5674, 87, 456, 1,123,15,35,7,5,8,579,7689,576,56,3456,43]
merge_sort(list_a, 0, (len(list_a) - 1))
print(list_a)
print(count)
