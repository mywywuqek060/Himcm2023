import numpy as np
import matplotlib.pyplot as plt

#变量表
r = 0.08  # 内在增长率
K = 800  # 环境承载上限
S_p = 3125  # 每一颗蒲公英每个月平均产生的种子数量
G_s = 0.0003  # 发芽率
alpha = 0.07  # 植物竞争对增长率的影响
beta = 0.07  # 动物竞争对增长率的影响
Ai = 1.3  # 动物的恒定正面影响
Cf = 1.2  # 气候因子（温带为1.0) 越高越好 
seasonal_factors = [1.1, 1.1, 1.1, 1.1, 1.0, 1.0, 1.0, 1.0, 1.1, 1.1, 1.1, 1.1]  

# 定义湿度和竞争特性 这部分有点儿玄学 但是图好看 于是就不改了 by mywywuqek060 2023.11.17
humidity_distribution = {'L': 0.2, 'M': 0.6, 'H': 0.2}  # 出现低中高湿度的概率
competition_distribution = {'L': 0.3, 'M': 0.4, 'H': 0.3}  # 出现低中高竞争的概率

# 定义基础公式
def calculate_population_probabilistic(Pn, r, K, Hf_dist, Cf, Pc_dist, Gs, Ai, alpha, beta, Sp, Sf):
    # 随机选择湿度与竞争环境
    Hf = np.random.choice(list(Hf_dist.keys()), p=list(Hf_dist.values()))
    Pc = np.random.choice(list(Pc_dist.keys()), p=list(Pc_dist.values()))
    
    Hf_factor = Hf_dist[Hf]
    Pc_factor = Pc_dist[Pc]
    # 储存单次计算结果
    return Pn * (1 + (r * Sf) * (1 - Pn / K) * (Hf_factor * Cf / (1 + (alpha * Pc_factor)))) + \
           (Sp * Sf) * Pn * Gs * Ai * (Hf_factor * Cf / (1 + (beta * Pc_factor)))

# 定义实验总数 初始化结果数组
num_simulations = 1000
months = np.arange(0, 13, 1)
monthly_populations = np.zeros((num_simulations, len(months)))

# 运算
initial_population = 1
for i in range(num_simulations):
    population = [initial_population]
    for month, Sf in zip(months[:-1], seasonal_factors):
        next_population = calculate_population_probabilistic(
            population[-1], r, K, humidity_distribution, Cf,
            competition_distribution, G_s, Ai, alpha, beta, S_p, Sf
        )
        # 确保种群大小不小于0
        next_population = max(next_population, 0)
        population.append(next_population)
    monthly_populations[i, :] = population

# 计算每个月的50%，75%和90%置信区间
percentile_50 = np.percentile(monthly_populations, [25, 75], axis=0)
percentile_75 = np.percentile(monthly_populations, [12.5, 87.5], axis=0)
percentile_90 = np.percentile(monthly_populations, [5, 95], axis=0)

# 使用不同蓝色的阴影绘制置信区间
plt.figure(figsize=(14, 8))
plt.fill_between(months, percentile_90[0, :], percentile_90[1, :], color='lightblue', alpha=0.5, label='90% Confidence Interval (CI)')
plt.fill_between(months, percentile_75[0, :], percentile_75[1, :], color='mediumblue', alpha=0.5, label='75% Confidence Interval (CI)')
plt.fill_between(months, percentile_50[0, :], percentile_50[1, :], color='darkblue', alpha=0.5, label='50% Confidence Interval (CI)')
plt.plot(months, np.median(monthly_populations, axis=0), color='navy', label='Median Population')
plt.title('Confidence Intervals for Dandelion Population Spread: Tropical')
plt.xlabel('Months')
plt.ylabel('Dandelion Population')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

# 计算每个月不同可能性区间的值域
confidence_intervals = {
    'Month': months,
    'Median': np.median(monthly_populations, axis=0),
    '90% Lower': percentile_90[0, :],
    '90% Upper': percentile_90[1, :],
    '75% Lower': percentile_75[0, :],
    '75% Upper': percentile_75[1, :],
    '50% Lower': percentile_50[0, :],
    '50% Upper': percentile_50[1, :],
}

# 打印结果 但是这个有问题 必须把图片关了之后才能显示打印的结果 应该是matplotlib库的问题 by mywywuqek060 2023.11.17
print("Month\tMedian\t90% Lower\t90% Upper\t75% Lower\t75% Upper\t50% Lower\t50% Upper")
for month in months:
    print(f"{int(month)}\t{confidence_intervals['Median'][int(month)]:.2f}\t{confidence_intervals['90% Lower'][int(month)]:.2f}\t{confidence_intervals['90% Upper'][int(month)]:.2f}\t{confidence_intervals['75% Lower'][int(month)]:.2f}\t{confidence_intervals['75% Upper'][int(month)]:.2f}\t{confidence_intervals['50% Lower'][int(month)]:.2f}\t{confidence_intervals['50% Upper'][int(month)]:.2f}")

