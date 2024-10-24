# Implementación del algoritmo

import random


# Definición de librerias requeridas


class Bandit:
    def __init__(self, num_arms=10, epsilon=0.9):
        self.arms = [random.uniform(-3, 3) for i in range(num_arms)]
        self.rewards = [0 for i in range(num_arms)]
        self.occurrences = [0 for i in range(num_arms)]
        self.cumulative_rewards = [0 for i in range(num_arms)]
        # definición nuevos atributos
        self.epsilon = epsilon
        self.epsilon_decay = 0.1

    def choose_arm(self):
        random.seed(7)
        rndm = random.uniform(0, 1)
        if rndm <= self.epsilon:
            arm = random.randint(0, len(self.arms) - 1)
        else:
            arm = self.rewards.index(max(self.rewards))
        return arm

    def expected_reward(self, arm):
        self.occurrences[arm] += 1
        reward = self.arms[arm]
        self.cumulative_rewards[arm] += reward
        self.rewards[arm] = self.cumulative_rewards[arm] / self.occurrences[arm]
        return self.rewards[arm]

    def run(self, episodes=1000):
        # your code here
        for i in range(episodes):
            if i % 100 == 0 and self.epsilon > 0:
                self.epsilon = self.epsilon - (self.epsilon * self.epsilon_decay)
                print(self.epsilon)
            arm = self.choose_arm()
            self.expected_reward(arm)

        return self.rewards


bandit =  Bandit(10, 0.9)
bandit.run()

print('arms', bandit.arms)
print('rewards', bandit.rewards)
print('cumulative_rewards', bandit.cumulative_rewards)
print('occurrences', bandit.occurrences)
print(bandit.epsilon)


