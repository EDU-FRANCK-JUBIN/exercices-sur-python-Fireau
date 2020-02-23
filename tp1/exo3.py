tt = [32, 5, 12, 8, 3, 75, 2, 15]
paired_list = []
impaired_list = []


for i in range(0, len(tt)):
    paired_list.append(tt[i]) if (
        tt[i] % 2 == 0) else impaired_list.append(tt[i])
    # (impaired_list.append(tt[i]), paired_list.append(tt[i]))[(tt[i] % 2 == 0)]
print(paired_list)
print(impaired_list)
