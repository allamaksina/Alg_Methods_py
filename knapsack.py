n, knapsack_volume = map(int, input().split())

staff = []

for _ in range(n):
    temp_price, temp_v = map(int, input().split())
    temp_price /= temp_v
    staff.append([temp_v, temp_price])

staff.sort(key=lambda z: z[1], reverse=True)
taken = 0

for i in range(n):
    if knapsack_volume:
        v = staff[i][0] - max(0, staff[i][0] - knapsack_volume)
        taken += staff[i][1] * v
        knapsack_volume -= v
    else:
        break

print(f'{taken:.3f}')
