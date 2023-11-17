import numpy as np
import matplotlib.pyplot as plt

r = 0.05
K = 1000
S_p = 50
G_s = 0.01
alpha = 0.05
beta = 0.05
Hf = {'L': 0.3, 'M': 1.0, 'H': 0.6}
Pc = {'L': 0.3, 'M': 0.7, 'H': 1.5}
Ai = 1.2
Cf_temperate = 1.0

seasonal_factors = [1.2, 1.2, 1.0, 1.0, 1.0, 0.8, 0.8, 0.8, 0.3, 0.3, 0.3, 1.2]

def calculate_population_seasonal(Pn, r, K, Hf, Cf, Pc, Gs, Ai, alpha, beta, Sp, Sf):
    return Pn * (1 + (r * Sf) * (1 - Pn / K) * (Hf * Cf / (1 + (alpha * Pc)))) + \
           (Sp * Sf) * Pn * Gs * Ai * (Hf * Cf / (1 + (beta * Pc)))

initial_population = 1
months = np.arange(0, 13, 1)
seasonal_results = {}

for humidity_level in Hf.keys():
    for competition_level in Pc.keys():
        population = [initial_population]
        for month, Sf in zip(months, seasonal_factors):
            next_population = calculate_population_seasonal(
                population[-1], r, K, Hf[humidity_level], Cf_temperate, 
                Pc[competition_level], G_s, Ai, alpha, beta, S_p, Sf
            )

            next_population = max(next_population, 0)
            population.append(next_population)
        seasonal_results[(humidity_level, competition_level)] = population

plt.figure(figsize=(14, 8))

for conditions, population in seasonal_results.items():
    plt.plot(months, population, label=f'Humidity: {conditions[0]}, Competition: {conditions[1]}')

plt.title('Seasonal Dandelion Population Spread in Temperate Climate')
plt.xlabel('Months')
plt.ylabel('Dandelion Population')
plt.legend()
plt.grid(True)
plt.show()
