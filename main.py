class Filme:
    def __init__(self, nome, ano, duracao):
        self.__name = nome.title()
        self.year = ano
        self.time = duracao
        self.__like = 0

    @property
    def like(self):
        return self.__like

    def give_likes(self):
        self.__like += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__name = nome.title()
        self.year = ano
        self.time = temporadas
        self.__like = 0

    @property
    def like(self):
        return self.__like

    def give_likes(self):
        self.__like += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()


vingadores = Filme('vingadores - Infinity war', 2018, 160)
vingadores.give_likes()

print(
    f'Nome: {vingadores.name} - Ano {vingadores.year} - Duracao do filme {vingadores.time} - Cutidas {vingadores.like}')

dark = Serie('Dark', 2018, 4)
dark.give_likes()
print(f'Nome: {dark.name} - Ano: {dark.year}- Temporadas: {dark.time} - Curtidas: {dark.like}')
