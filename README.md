# Dining-Philosophers-Problem
The Dining Philosophers Problem demonstra a complexidade da sincronização 
de múltiplas threads competindo por recursos compartilhados (os garfos).
Ele é um modelo clássico de sistemas concorrentes.

Funcionamento:

Cada filósofo alterna entre pensar e comer.

Para comer, um filósofo precisa pegar dois garfos (um à esquerda e outro à direita).

Mutexes (ou locks) são usados para evitar que dois filósofos usem o mesmo garfo simultaneamente.

Estratégias como restrição ou prioridade podem ser usadas para evitar deadlocks.
