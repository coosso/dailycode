def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # 初始化指针：i指向nums1有效元素末尾，j指向nums2末尾，k指向合并后数组末尾
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1  # 移动nums1指针
        else:
            nums1[k] = nums2[j]
            j -= 1  # 移动nums2指针
    k -= 1  # 移动合并后数组指针

    # 若nums2还有剩余元素，直接复制到nums1（nums1剩余元素已在正确位置）
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
merge(nums1, m, nums2, n)
# 期望输出: [1]
# 原代码会报错: 索引i=-1访问nums1[i]

merge(nums1, m, nums2, n)
print(nums1)
