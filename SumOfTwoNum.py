import numpy as np
import math
nums = [0,4,3,0]


def TwoSum(nums, target):
    ind = []
    lcnt = 0
    for i in range(len(nums)):
        findx = target - nums[i]
        lcnt += 1
        bCnt = 0
        # ret, val, cnt = Search(nums[(i+1):], findx, 0, len(nums[(i+1):])-1, bCnt)
        # lcnt += cnt
        if lnSearch(nums[(i+1):], findx):
            ind.append(i)
            ind.append(nums.index(findx, (i + 1), len(nums)))
            break

        # if ret != -1:
        #     ind.append(i)
        #     ind.append(nums.index(val, (i+1), len(nums)))
        #     break

    return ind, lcnt


def lnSearch(arr, key):
    for k in range(len(arr)):
        if arr[k] == key:
            return True

    return False


def Search(a, key, low, high, bCnt):
    if high >= low:
        mid = round((high + low)/2)
        bCnt += 1
        # if mid <= -1 or mid == 0:
        #     return -1, -1, bCnt

        if a[mid] == key:
            return mid, a[mid], bCnt
        elif a[mid] > key:
            return Search(a, key, low, mid-1, bCnt)
        else:
            return Search(a, key, mid+1, high, bCnt)
    else:
        return -1, -1, bCnt


print(TwoSum(nums, 0))

