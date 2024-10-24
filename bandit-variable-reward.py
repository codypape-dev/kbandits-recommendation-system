# Implementación del algoritmo
import math
import random

# Definición de librerias requeridas


class Bandit:
    def __init__(self, num_arms=10, epsilon=0.9, alpha=0.1):
        self.epsilon = epsilon
        self.arms = [random.uniform(-3, 3) for i in range(num_arms)]
        self.rewards = [0 for i in range(num_arms)]
        # definición nuevos atributos
        self.alpha = alpha
        self.epsilon = epsilon
        self.epsilon_decay = 0.1
        self.episode_rewards = []

        for i in range(num_arms):
            self.episode_rewards.append([])

    def choose_arm(self):
        rndm = random.uniform(0, 1)
        if rndm <= self.epsilon:
            arm = random.randint(0, len(self.arms) - 1)
        else:
            arm = self.rewards.index(max(self.rewards))
        return arm

    def expected_reward(self, arm, episode):
        reward = self.arms[arm]
        self.episode_rewards[arm].append(reward * math.sin(episode))
        return self.episode_rewards[arm][-1]

    def calculate_expected_reward1(self, arm: int):
        qn = self.rewards[arm]
        n = len(self.episode_rewards[arm])
        q_i = qn + self.alpha * (self.episode_rewards[arm][-1] - qn)
        print('calculate_expected_reward1', q_i)
        return q_i

    def calculate_expected_reward3(self, arm: int):

        q1 = 0
        n = len(self.episode_rewards[arm])

        qn = (1 - self.alpha) ** n
        qn = qn * q1
        summ_rewards = 0
        for i in range(1, n + 1):
            r = self.episode_rewards[arm][i - 1]
            rw = (self.alpha * (1 - self.alpha) ** (n - i)) * r
            summ_rewards += rw

        qn = qn + summ_rewards
        print('calculate_expected_reward3', qn)

        self.rewards[arm] = qn

        return qn

    def run(self, episodes=1000):
        for i in range(episodes):
            if i % 100 == 0 and self.epsilon > 0:
                self.epsilon = self.epsilon - (self.epsilon * self.epsilon_decay)
            arm = self.choose_arm()
            self.expected_reward(arm, i)
            self.calculate_expected_reward1(arm)
            self.calculate_expected_reward3(arm)

        return self.rewards

if __name__ == '__main__':
    bandit =  Bandit(3, 0.9)
    bandit.run(10)
    print('arms', bandit.arms)
    print('rewards', bandit.rewards)
    print('epsilon', bandit.epsilon)
    print('episode_rewards', bandit.episode_rewards)
