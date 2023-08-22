from banco import obterConta, banco

def consultaSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if conta:
        print(f"Seu saldo: R$ {cliente['saldo']}")
    else:
        print('Conta não existe!')

if __name__ == "__main__":
    consultaSaldo(1)
    print(banco)