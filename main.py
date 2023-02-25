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


class Filme(Program):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.time = duracao


class Serie(Program):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.time = temporadas


vingadores = Filme('vingadores - Infinity war', 2018, 160)
vingadores.give_likes()

print(
    f'{vingadores.name} - {vingadores.year} - {vingadores.time} - {vingadores.like}')

dark = Serie('Dark', 2018, 4)
dark.give_likes()
print(
    f'{dark.name} - {dark.year} - {dark.time} - {dark.like}')
