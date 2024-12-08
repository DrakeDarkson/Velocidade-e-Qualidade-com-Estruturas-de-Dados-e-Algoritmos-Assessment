import random
import time

def bubble_sort(prices):
    n = len(prices)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if prices[j] > prices[j + 1]:
                prices[j], prices[j + 1] = prices[j + 1], prices[j]

prices_1k = [random.randint(1, 10000) for _ in range(1000)]
prices_10k = [random.randint(1, 10000) for _ in range(10000)]

# Teste com mil elementos
start_time = time.time()
bubble_sort(prices_1k)
time_1k = time.time() - start_time
print(f"Tempo de execução para 1 mil elementos: {time_1k:.4f} segundos.")

# Teste com 10 mil elementos
start_time = time.time()
bubble_sort(prices_10k)
time_10k = time.time() - start_time
print(f"Tempo de execução para 10 mil elementos: {time_10k:.4f} segundos.")
