class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, trabalho):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.trabalho = float(trabalho)


class Media:
    def media(self, aluno):
        # Peso: prova1 = 2.5, prova2 = 2.5, trabalho = 2 → total = 7
        return ((aluno.nota1 * 2.5) + (aluno.nota2 * 2.5) + (aluno.trabalho * 2)) / 7

    def final(self, aluno):
        media = self.media(aluno)

        if media >= 6:
            return 0
        else:
            return 6 - media

    def calcular_media(self, nota1, nota2, trabalho):
        # método auxiliar para o controller
        aluno_temp = Aluno("temp", "temp", nota1, nota2, trabalho)
        return self.media(aluno_temp)