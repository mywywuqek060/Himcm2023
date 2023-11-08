import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the temperate climate with seasonal effects
r = 0.05  # Intrinsic growth rate
K = 1000  # Carrying capacity of the environment
S_p = 50  # Average number of seeds produced per plant per month
G_s = 0.01  # Seed production growth function
alpha = 0.05  # Nonlinearity in competition
beta = 0.05  # Nonlinearity in animal interaction
Hf = {'L': 0.3, 'M': 1.0, 'H': 0.6}  # Humidity factors
Pc = {'L': 0.3, 'M': 0.7, 'H': 1.5}  # Plant competition factors
Ai = 1.2  # Animal interaction factor (constant positive effect)
Cf_temperate = 1.0  # Climate factor for temperate climate

# Define the seasonal factors assuming the sequence starts with Spring
seasonal_factors = [1.2, 1.2, 1.0, 1.0, 1.0, 0.8, 0.8, 0.8, 0.3, 0.3, 0.3, 1.2]  # Spring, Summer, Autumn, Winter

# ... [之前的代码保持不变] ...

# Function to calculate the next month's population with seasonal adjustment
def calculate_population_seasonal(Pn, r, K, Hf, Cf, Pc, Gs, Ai, alpha, beta, Sp, Sf):
    return Pn * (1 + (r * Sf) * (1 - Pn / K) * (Hf * Cf / (1 + (alpha * Pc)))) + \
           (Sp * Sf) * Pn * Gs * Ai * (Hf * Cf / (1 + (beta * Pc)))

# Simulate over 12 months with initial population, including the 12th month
initial_population = 1
months = np.arange(0, 13, 1)  # Include month 12
seasonal_results = {}

# Run the simulation for different combinations of humidity and plant competition with seasonal effects
for humidity_level in Hf.keys():
    for competition_level in Pc.keys():
        population = [initial_population]
        for month, Sf in zip(months, seasonal_factors):  # Use the full months array and seasonal_factors
            next_population = calculate_population_seasonal(
                population[-1], r, K, Hf[humidity_level], Cf_temperate, 
                Pc[competition_level], G_s, Ai, alpha, beta, S_p, Sf
            )
            # Ensure the population doesn't go below zero
            next_population = max(next_population, 0)
            population.append(next_population)
        seasonal_results[(humidity_level, competition_level)] = population

# Plot the results with seasonal effects, including the 12th month
plt.figure(figsize=(14, 8))

for conditions, population in seasonal_results.items():
    plt.plot(months, population, label=f'Humidity: {conditions[0]}, Competition: {conditions[1]}')

plt.title('Seasonal Dandelion Population Spread in Temperate Climate')
plt.xlabel('Months')
plt.ylabel('Dandelion Population')
plt.legend()
plt.grid(True)
plt.show()
