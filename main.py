names = ["TOI", "Hindu", "ET", "BM", "HT"]
prices = [26, 20.5, 34, 10.5, 18]
f = 0
ans = {}
print('Enter budget:')
s = float(input())
for i in range(5):
    for j in range(5):
        if i != j:
            if prices[i] + prices[j] <= s:
                if (names[j], names[i]) not in ans.items():
                    ans.update({names[i]: names[j]})
                f = 1
if f != 1:
    print('budget not enough')
for k, v in ans.items():
    print({k, v})
