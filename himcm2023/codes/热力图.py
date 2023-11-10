import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# 设置模型参数
seed_production = 10  # 每个蒲公英每月产生的种子数量
dispersion_std_dev = 5  # 种子扩散的标准差（格子单位）
germination_rate = 0.05  # 种子萌发率
grid_size = 50  # 网格大小

# 初始化网格
grid = np.zeros((grid_size, grid_size))
grid[grid_size // 2, grid_size // 2] = 1  # 在中心放置一个蒲公英

# 定义一个函数来模拟蒲公英的扩散
def simulate_dandelion_spread(grid, months):
    for _ in range(months):
        # 计算当前的蒲公英数量
        current_dandelions = np.sum(grid)

        # 计算新产生的种子数量
        new_seeds = current_dandelions * seed_production

        # 模拟种子扩散
        seeds_dispersion = np.random.normal(0, dispersion_std_dev, (int(new_seeds), 2))
        for seed in seeds_dispersion:
            x, y = int(grid_size // 2 + seed[0]), int(grid_size // 2 + seed[1])
            if 0 <= x < grid_size and 0 <= y < grid_size:
                grid[x, y] += germination_rate

        # 模糊网格以模拟风力扩散
        grid = gaussian_filter(grid, sigma=1)

    return grid

# 运行模型并生成热力图
months = [1, 2, 3, 6, 12]
fig, axes = plt.subplots(1, len(months), figsize=(20, 4))

for i, month in enumerate(months):
    spread_grid = simulate_dandelion_spread(grid.copy(), month)
    axes[i].imshow(spread_grid, cmap='hot', interpolation='nearest')
    axes[i].set_title(f"{month} Months")
    axes[i].axis('off')

plt.tight_layout()
plt.show()
