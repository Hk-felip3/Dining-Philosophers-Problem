
def dining_philosophers():
    import threading
    import time

    num_philosophers = 5
    forks = [threading.Lock() for _ in range(num_philosophers)]

    def philosopher(i):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % num_philosophers]

        while True:
            print(f"Filósofo {i} está pensando.")
            time.sleep(1)
            print(f"Filósofo {i} quer comer.")
            with left_fork:
                with right_fork:
                    print(f"Filósofo {i} está comendo.")
                    time.sleep(1)

    threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(num_philosophers)]
    for thread in threads:
        thread.start()