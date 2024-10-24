'''
Suponga que vamos a ofrecer un sistema de recomendación para películas dentro de una plataforma de alquiler de películas
por internet. El sistema recomienda cuatro películas (p1, p2, p3, p4) a los clientes (20 en nuestro caso), que pagarán
el valor de la película más una propina variable (entre el valor de la película y 1.5 veces el valor de la película,
es decir un número entre 10 y 15) si esta les gusta. Sin embargo, los usuarios no pagarán nada si la película no les gusta.

Queremos calcular el valor estimado del alquiler de cada una de las películas (la recompensa) si todas
 las películas tienen un valor inicial de 10$.

Sabemos que a los clientes 1, 3, 4, 11, 12, 13 y 18 no les gustará la película. Todos los otros clientes gustarán
 de la película recomendada. La propina para cada uno de ellos se calcula como:

 max(número de cliente por número de la película / 2, 5)

 Además, sabemos que las películas serán recomendadas en el siguiente orden
 [4,2,3,3,3,1,4,2,1,2,3,3,2,2,3,4,4,4,3,1] para los clientes.

Suponga un valor de paso α de 0.1

Bajo estas condiciones queremos determinar el valor estimado total de cada película.

De su respuesta especificando el valor q de cada uno de los caminos separados por comas.
Utilice máximo dos puntos decimales si lo necesita (e.g., q(p1)=10.00, q(p2)=10.00, q(p3)=10.00, q(p4)=10.00)
'''
import numpy as np

movies_summ_reward = {1:0, 2:0, 3:0, 4:0}
movies_reward = []
movies_count = {1:0, 2:0, 3:0, 4:0}
clients = [i for i in range(1, 21)]
movie_order = [4,2,3,3,3,1,4,2,1,2,3,3,2,2,3,4,4,4,3,1]
rewards = [0] * 20
rewards_cumulative = [0] * 20

a = 0.1
rewards_cumulative[0] = 10
n = 4

for i in range(0, 20):
    rewards[i] = min((clients[i]*movie_order[i])/2, 5) + 10
    if i in [0, 2, 3, 10, 11, 12, 17]:
        rewards[i] = 0

print('rewards', rewards, len(rewards))
print('movie_order', movie_order, len(movie_order))
print('clients', clients, len(clients))

def q(n: int):
    qn = rewards_cumulative[n]
    q = qn + (a * (rewards[n] - qn))
    return q

for i in range(0, 19):
    qn1 = q(i)
    rewards_cumulative[i + 1] = qn1

reward_movie = np.dot(movie_order, rewards_cumulative)

for i in range(0, 20):
    movie_showing = movie_order[i]
    reward = rewards_cumulative[i]
    movies_summ_reward[movie_showing] += reward
    movies_count[movie_showing] += 1


for i in range(1,5):
    movie_summ = movies_summ_reward[i]
    movie_count = movies_count[i]
    res = movie_summ / movie_count
    movies_reward.append(round(res, 2))

print('rewards_cumulative', rewards_cumulative)
print('movies_summ_reward', movies_summ_reward)
print('movies_count', movies_count)
print('movies_reward', movies_reward)


