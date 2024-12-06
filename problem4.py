
def bubble_Sort(lists):
    for _ in range (len(lists)-1):
        for i in range(len(lists)-1):
            if lists[i+1] < lists[i]:
                temp = lists[i]
                lists [i] = lists[i+1]
                lists[i+1] = temp
    return lists


def selection_Sort(lists):
    for j in range(len(lists)):
        smallest_Value = lists[j]
        for i,ang in enumerate(lists[j:]):
            if ang < smallest_Value:
                smallest_Value = ang
                smallest_Index = i
        temp = lists[j]
        lists[j] = lists[smallest_Index]
        lists[smallest_Index] = temp
    return lists

list_Nilai = [
    85, 13, 99, 34, 71, 15, 82, 24, 64, 61, 67, 99, 50, 68, 25, 37, 32,
    27, 14, 91, 79, 15, 47, 48, 74, 88,
    64, 53, 77, 50, 24, 91, 87, 55, 60, 75, 91, 22, 47, 63, 81, 88, 26, 48, 69,
    59, 84, 77, 28, 36, 59, 74, 89, 73,
    91, 64, 55, 88, 90, 48, 73, 97, 98, 40, 93, 50, 78, 60, 44, 77, 82, 51, 53,
    65, 98, 59, 94, 91, 52, 44, 65, 85,
    72, 92, 49, 67, 58, 48, 62, 54, 89, 67, 58, 48, 85, 45, 77, 76, 81, 77
]

used_Lists1 = list_Nilai.copy()
ln_Bubbles = bubble_Sort(used_Lists1)

used_Lists2 = list_Nilai.copy()
ln_Selects = selection_Sort(used_Lists2)

print("The Unsorted Lists")
print(list_Nilai)

print("\nThe Sorted Lists with Bubble Sorts")
print(f"{ln_Bubbles}")

print("\nThe Sorted Lists with Selection Sorts")
print(f"\n{ln_Selects}")