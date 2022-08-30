word = "TRY"
ans = []

for i in range(len(word)):
    for j in range(len(word)):
        for k in range(len(word)):
            if i == j or j == k or k == i:
                continue
            ans.append(word[i]+word[j]+word[k])

print(ans)
