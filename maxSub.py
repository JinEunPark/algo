input = [1,-4,3,2]
MAX_FINAL = -100000


def find_max_corssing_subArray(input, low, mid, high):
    leftSum = MAX_FINAL
    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + input[i]
        if sum > leftSum:
            leftSum = sum
            max_left = i
    rightSum = MAX_FINAL
    sum = 0
    for j in range(mid+1, high + 1):
        sum = sum + input[j]
        if sum > rightSum:
            rightSum = sum
            max_right = j
    return (max_left, max_right, leftSum + rightSum)


def find_max_subArray(input, low, high):
    if high == low:
        return (low, high, input[low])
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = find_max_subArray(input, low, mid)
        (right_low, right_high, right_sum) = find_max_subArray(input, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_corssing_subArray(input, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

result = find_max_subArray(input,0,len(input)-1)
print(result)
