def binary_search(arr, target, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


if __name__ == "__main__":
    arr = (-5, -3, 0, 4, 20)
    test_cases = {
        -5: 0,
        -3: 1,
        0: 2,
        4: 3,
        20: 4,
        100: None,
        -100: None
    }

    for num, expected in test_cases.items():
        assert binary_search(arr, num, 0, len(arr) - 1) == expected, f"Wrong at {num}"
    print("All tests passed!")