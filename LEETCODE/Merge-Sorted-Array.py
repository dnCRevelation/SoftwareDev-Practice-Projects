class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2[:n])
        