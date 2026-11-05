import time
import random

def merge_sort(arr):
    """Implementação clássica de Merge Sort (garante O(n log n) no pior caso)."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Testando o crescimento do tempo conforme n aumenta
tamanhos = [1000, 10000, 50000, 100000, 200000]

print(f"{'Tamanho (n)':<12} | {'Tempo (segundos)':<15}")
print("-" * 32)

for n in tamanhos:
    # Cria uma lista com n números aleatórios
    dados = [random.randint(1, 1000000) for _ in range(n)]
    
    inicio = time.time()
    merge_sort(dados)
    fim = time.time()
    
    tempo_gasto = fim - inicio
    print(f"{n:<12} | {tempo_gasto:.6f} s")