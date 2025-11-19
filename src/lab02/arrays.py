def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if len(nums) <= 0:
        raise ValueError
    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:

    nums = set(nums)
    nums = list(nums)
    return nums


def flatten(mat: list[list | tuple]) -> list:

    true_mat = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            raise TypeError
        for k in i:
            if isinstance(k, str):
                raise TypeError

    for i in range(len(mat)):
        for k in mat[i]:
            true_mat.append(k)
    return true_mat
