import matplotlib.pyplot as plt

# 蒲公英 Dandelion
S_dandelion = 3125  # 月新增植株数量
ω_s_dandelion = 0.2  # 新增植株数量的权重
C_dandelion = 200  # 每月的管理和控制成本
ω_c_dandelion = 0.4  # 管理和控制成本的权重
A_dandelion = 0  # 是否是过敏原
ω_a_dandelion = 400  # 是否是过敏原的权重

# 山艾蒿 Common Ragweed
S_ragweed = 815  # 月新增植株数量
ω_s_ragweed = 0.2 # 新增植株数量的权重
C_ragweed = 300  # 每月的管理和控制成本
ω_c_ragweed = 0.4  # 管理和控制成本的权重
A_ragweed = 1  # 是否是过敏原
ω_a_ragweed = 400  # 是否是过敏原的权重

# 日本虫子草 Japanese Knotweed
S_knotweed = 1520  # 月新增植株数量
ω_s_knotweed = 0.2  # 新增植株数量的权重
C_knotweed = 500  # 每月的管理和控制成本
ω_c_knotweed = 0.4  # 管理和控制成本的权重
A_knotweed = 0  # 是否是过敏原
ω_a_knotweed = 400  # 是否是过敏原的权重

I_dandelion = ω_s_dandelion * S_dandelion + ω_c_dandelion * C_dandelion + ω_a_dandelion * A_dandelion
I_ragweed = ω_s_ragweed * S_ragweed + ω_c_ragweed * C_ragweed + ω_a_ragweed * A_ragweed
I_knotweed = ω_s_knotweed * S_knotweed + ω_c_knotweed * C_knotweed + ω_a_knotweed * A_knotweed

plants = ['Dandelion', 'Common Ragweed', 'Japanese Knotweed']
I_values = [I_dandelion*0.01, I_ragweed*0.01, I_knotweed*0.01]

print(I_values)

plt.bar(plants, I_values, color='lightblue') 
plt.ylabel('Impact Factor (I)')
plt.title('Impact Factor Comparison')
plt.show()


