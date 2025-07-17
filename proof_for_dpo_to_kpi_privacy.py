import numpy as np
import matplotlib.pyplot as plt

def simulate_preference_regret(delta=1.0, epsilons=np.linspace(0.1, 3, 20)):
    regret = []
    for eps in epsilons:
        b = delta / eps
        prob = np.exp(-delta / (2 * b))  # error probability
        regret.append(prob)
    return epsilons, regret

eps, regret = simulate_preference_regret()
plt.plot(eps, regret)
plt.xlabel("Privacy budget (ε)")
plt.ylabel("Preference Regret")
plt.title("Tradeoff: Privacy vs Preference Accuracy")
plt.grid(True)
plt.show()
