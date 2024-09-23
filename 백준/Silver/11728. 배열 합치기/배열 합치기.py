import sys
input = sys.stdin.read

def merge_arrays(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    # 남은 요소들을 추가
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

# 입력 처리
data = input().split()
N, M = int(data[0]), int(data[1])
arr1 = list(map(int, data[2:N+2]))
arr2 = list(map(int, data[N+2:]))

# 배열 병합
merged_array = merge_arrays(arr1, arr2)

# 결과 출력
print(' '.join(map(str, merged_array)))