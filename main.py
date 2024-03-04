from typing import List
import time
import numpy as np

def sort(li: list):
    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                temp = li[j]
                li[j] = li[j + 1]
                li[j + 1] = temp
    return li

def fourSum_enumeration(nums:list[int],target:int):
    if len(nums)<4:
        print("输入有误！")
        return

    res = set()
    n = len(nums)
    for first in range(0, n-3):
        for second in range(first+1, n-2):
            for third in range(second+1, n-1):
                for forth in range(third+1, n):
                    if nums[first] + nums[second] + nums[third] + nums[forth] == target:
                        res.add((nums[first], nums[second], nums[third], nums[forth]))

    return res


def fourSum_pointer(nums: list[int], target: int):
    if len(nums) < 4:
        print("输入有误！")
        return
    nums.sort()
    n = len(nums)
    res = []
    for first in range(0, n - 3):
        if nums[first] + nums[first + 1] + nums[first + 2] + nums[first + 3] > target:
            break
        if nums[first] == nums[first - 1]:
            continue
        if nums[first] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue
        for second in range(first + 1, n - 2):
            if nums[first] + nums[second] + nums[second + 1] + nums[second + 2] > target:
                break
            if nums[second] == nums[second - 1]:
                continue
            if nums[first] + nums[second] + nums[n - 2] + nums[n - 1] < target:
                continue
            left = second + 1
            right = n - 1
            while left < right:
                sum = nums[first] + nums[second] + nums[left] + nums[right]
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                elif sum == target:
                    res.append([nums[first], nums[second], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

    return res


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []

        def Search(i, target, oneSolution, notSelected):
            if target == 0 and len(oneSolution) == 4:
                output.append(oneSolution)
                return
            elif len(oneSolution) > 4 or i >= len(nums):
                return

            if target - nums[i] - (3 - len(oneSolution)) * nums[-1] > 0 or nums[i] in notSelected:
                Search(i + 1, target, oneSolution, notSelected)
            elif target - (4 - len(oneSolution)) * nums[i] < 0:
                return
            else:
                Search(i + 1, target, oneSolution, notSelected + [nums[i]])
                Search(i + 1, target - nums[i], oneSolution + [nums[i]], notSelected)

        Search(0, target, [], [])

        return output


# 输入希望得到的n数之和，数组,目标值和指针所在位置
def nSum(n: int, nums: list[int], target: int, pos: int):
    if n < 2 or len(nums) < n:
        print("输入有误！")
        return
    nums.sort()
    size = len(nums)
    res = []
    if n == 2:
        low = pos
        high = size - 1
        while low < high:
            sum = nums[low] + nums[high]
            left = nums[low]
            right = nums[high]
            if sum < target:
                low += 1
            elif sum > target:
                high -= 1
            else:
                res.append([left, right])  # 以list形式加到res中
                while low < high and nums[low] == left:
                    low += 1
                while low < high and nums[high] == right:
                    high -= 1

    else:
        i = pos
        while i < size:
            subs = nSum(n - 1, nums, target - nums[i], i + 1)
            for elem in subs:
                elem.append(nums[i])
                res.append(elem)
            while i < size - 1 and nums[i] == nums[i + 1]:
                i = i + 1
            i += 1

    return res


if __name__=="__main__":
    '''
    nums=[]
    nums=input('请输入数组：').strip(',').split(',')
    nums=[int(num) for num in nums]
    target=int(input('请输入求和预期值:'))
    n=int(input('请输入求和元组的元素个数:'))
    res_set = set()
    res_list = list()
    pos = 0
    print('四数之和实现方法一(暴力枚举法)：')
    t_start = time.time()  # float
    res_set = fourSum_enumeration(nums, target)
    t_end = time.time()
    print('枚举方法耗时{:.4f}'.format(t_end - t_start))
    print(res_set)
    print('四数之和实现方法二(双指针法)：')
    t_start = time.time()
    res_list = fourSum_pointer(nums, target)
    t_end = time.time()
    print('双指针方法耗时{:.4f}'.format(t_end - t_start))
    print('一共找到'+str(len(res_set))+'个四元组满足和为0')
    print(res_list)
    solution=Solution()
    t_start = time.time()
    res_list = solution.fourSum(nums, target)
    t_end = time.time()
    print('回溯法耗时{:.4f}'.format(t_end - t_start))
    print('一共找到' + str(len(res_set)) + '个四元组满足和为0')
    print(res_list)
    #拓展，实现n数之和
    res=[]
    t_start = time.time()
    res = nSum(n, nums, target, pos)
    t_end = time.time()
    print('DFS法耗时{:.4f}'.format(t_end - t_start))
    print('使用nSum函数得到的n数之和的数组：')
    for i in range(len(res)):
        print(res[i])
    '''

    #print('\n\n大数据测试：')
    solution = Solution()
    nums = np.random.randint(-10, 10, 1000)
    nums=nums.tolist()
    target = 0
    res_set = set()
    res_list = list()
    #t_start = time.time()
    #res_set = fourSum_enumeration(nums, target)
    #t_end = time.time()
    #print('枚举方法耗时{:.4f}'.format(t_end - t_start))
    t_start = time.time()  # float
    res_list = fourSum_pointer(nums, target)
    t_end = time.time()
    print('双指针方法耗时{:.4f}'.format(t_end - t_start))
    t_start = time.time()  # float
    res_list = solution.fourSum(nums, target)
    t_end = time.time()
    print('回溯法耗时{:.4f}'.format(t_end - t_start))
    #print('符合条件的元组：' + str(len(res_list)))
    t_start = time.time()  # float
    res_list = nSum(4, nums, target, 0)
    t_end = time.time()
    print('DFS方法耗时{:.4f}'.format(t_end - t_start))
    print('符合条件的元组：'+str(len(res_set)))

