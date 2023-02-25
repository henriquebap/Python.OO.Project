class Program:
    def __init__(self, nome, ano):
        self._name = nome.title()
        self.year = ano
        self._likes = 0

    @property
    def like(self):
        return self._likes

    def give_likes(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return f'{self._name} - {self.year} - {self.like} Likes'


class Filme(Program):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._name} - {self.year} - {self.duracao} Minutos - {self.like} Likes'


class Serie(Program):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporada = temporadas

    def __str__(self):
        return f'{self._name} - {self.year} - {self.temporada} Temporadas - {self.like} Likes'


filme_1 = Filme('vingadores - Infinity war', 2018, 160)
filme_1.give_likes()

serie_1 = Serie('Dark', 2018, 4)
serie_1.give_likes()

filmes_e_series = [filme_1, serie_1]

for Program in filmes_e_series:
    print(Program)
