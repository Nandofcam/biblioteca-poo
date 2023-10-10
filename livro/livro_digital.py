from livro import Livro

class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano_publicacao, formato):
        super().__init__(titulo, autor, ano_publicacao)
        self.formato = formato

    def __repr__(self):
        return f"Id: {self.id} \n" \
               f"Título: {self.titulo} \n" \
               f"Autor: {self.autor} \n" \
               f"Ano de publicação: {self.ano_publicacao} \n" \
               f"Formato do arquivo: {self.formato}"
    
if __name__ == "__main__":
    livroD = LivroDigital("Harry Potter", "J K Rolling", 1997, "PDF")

    print(livroD)