def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m - 1
    j = n - 1
    for x in range(m + n - 1, -1, -1):
        if nums1[i] >= nums2[j]:
            nums1[x] = nums1[i]
            i = i - 1
        else:
            nums1[x] = nums2[j]
            j = j - 1
        if i < 0 or j < 0:
            break


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)
