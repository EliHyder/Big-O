import time

def gerar_permutacoes(arr):
    """Gera todas as permutações possíveis (Complexidade O(n!))."""
    if len(arr) <= 1:
        return [arr]
    
    permutacoes = []
    for i in range(len(arr)):
        atual = arr[i]
        resto = arr[:i] + arr[i+1:]
        for p in gerar_permutacoes(resto):
            permutacoes.append([atual] + p)
    return permutacoes

# Testando com valores pequenos de n
tamanhos = [1, 3, 5, 8, 10]

print(f"{'Tamanho (n)':<12} | {'Nº de Permutações (n!)':<22} | {'Tempo (segundos)':<15}")
print("-" * 57)

for n in tamanhos:
    dados = list(range(n))
    
    inicio = time.time()
    gerar_permutacoes(dados)
    fim = time.time()
    
    tempo_gasto = fim - inicio
    
    # Cálculo manual do fatorial para exibir na tabela
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
        
    print(f"{n:<12} | {fatorial:<22} | {tempo_gasto:.6f} s")