class PalavrasObserver:
    def update(self, frase):
        palavras = frase.split()
        total_palavras = len(palavras)
        palavras_pares_caracteres = 0
        palavras_maiusculas = 0

        for palavra in palavras:
            if len(palavra) % 2 == 0:
                palavras_pares_caracteres += 1
            if palavra[0].isupper():
                palavras_maiusculas += 1

        print(f"Total de palavras: {total_palavras}")
        print(f"Palavras com quantidade par de caracteres: {palavras_pares_caracteres}")
        print(f"Palavras começadas com maiúsculas: {palavras_maiusculas}")


class ContadorPalavras:
    def __init__(self):
        self._observers = []

    def adicionar_observer(self, observer):
        self._observers.append(observer)

    def remover_observer(self, observer):
        self._observers.remove(observer)

    def contar_palavras(self, frase):
        for observer in self._observers:
            observer.update(frase)


if __name__ == "__main__":
    frase = input("Digite uma frase: ")

    contador_palavras = ContadorPalavras()
    observer = PalavrasObserver()
    contador_palavras.adicionar_observer(observer)

    contador_palavras.contar_palavras(frase)
