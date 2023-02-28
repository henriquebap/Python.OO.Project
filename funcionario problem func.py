class Funcionarios:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas....')

    def mostrar_tarefas(self):
        print('Fez muitas tarefas....')


class Caelum(Funcionarios):
    def mostrar_tarefas(self):
        print('Fez muitas tarefas, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mosntrando Cursos - {mes}' if mes else 'Mostrando cursos desse mes')


class Alura(Funcionarios):
    def mostrar_tarefas(self):
        print('Quanta coisa realizada, alura!!!')

    def buscar_perguntas_sem_resposta(self):
        print('Mostrando Perguntas nao respondidas do forum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum, Hipster):
    pass


class Senior(Alura, Caelum):
    pass


jose = Junior('Jose')
jose.buscar_perguntas_sem_resposta()

Luan = Pleno('Luan')
print(Luan)

Luan.buscar_perguntas_sem_resposta()
Luan.busca_cursos_do_mes()