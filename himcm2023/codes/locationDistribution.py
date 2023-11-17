import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

seed_production = 50
dispersion_std_dev = 1.3
germination_rate = 0.02
grid_size = 16
wind_direction_bias = (3, 3)

# 初始化网格
grid = np.zeros((grid_size, grid_size))
grid[grid_size // 2, grid_size // 2] = 1

def simulate_dandelion_spread_with_wind(grid, months, wind_bias):
    max_grid = grid.copy()  # 用于记录最大值，确保颜色不变浅 - 这个有问题，by mywywuqek060 2023.11.17
    for _ in range(months):
        current_dandelions = np.sum(grid)
        new_seeds = current_dandelions * seed_production

        # 模拟有风影响的种子扩散
        for _ in range(int(new_seeds)):
            seed_dispersion = np.random.normal(0, dispersion_std_dev, 2) + wind_bias
            x, y = int(grid_size // 2 + seed_dispersion[0]), int(grid_size // 2 + seed_dispersion[1])
            if 0 <= x < grid_size and 0 <= y < grid_size:
                grid[x, y] += germination_rate

        # 在较小网格上进行轻微的模糊处理
        grid = gaussian_filter(grid, sigma=0.5)
        max_grid = np.maximum(max_grid, grid)  # 更新最大值

    return max_grid

months = [1, 2, 3, 6, 12]
fig, axes = plt.subplots(1, len(months), figsize=(20, 4))

for i, month in enumerate(months):
    spread_grid = simulate_dandelion_spread_with_wind(grid.copy(), month, wind_direction_bias)
    axes[i].imshow(spread_grid, cmap='Blues', interpolation='nearest', extent=[0, grid_size, 0, grid_size])
    
#costumize效果
    axes[i].grid(which='major', axis='both', linestyle='-', color='black', linewidth=0.5)
    axes[i].set_xticks(np.arange(0, grid_size, 1))
    axes[i].set_yticks(np.arange(0, grid_size, 1))

    axes[i].set_title(f"{month} Months")
    axes[i].axis('off')

plt.tight_layout()
plt.show()