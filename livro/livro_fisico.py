from livro.livro import Livro

class LivroFisico(Livro):
    def __init__(self, titulo, autor, ano_publicacao, num_paginas):
        super().__init__(titulo, autor, ano_publicacao)
        self.num_paginas = num_paginas
    def __repr__(self):
        return f"Id: {self.id} \n" \
               f"Título: {self.titulo} \n" \
               f"Autor: {self.autor} \n" \
               f"Ano de publicação: {self.ano_publicacao} \n" \
               f"Nº de páginas: {self.num_paginas}"

if __name__ == "__main__":
    livrof = LivroFisico("Harry Potter", "J K Rolling", 1997, 300)
    print(livrof)