from services.media import Media, Aluno

class CalculadorMedia:

    def __init__(self, start=0):
        pass

    def calcular(self, nota1, nota2, trabalho):
        media = Media()

        resultado = media.calcular_media(
            nota1,
            nota2,
            trabalho
        )

        return resultado


c = CalculadorMedia()