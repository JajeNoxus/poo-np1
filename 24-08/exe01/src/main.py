from services.media import Aluno, Media
from controllers.calcular_media import CalculadorMedia

def main():
    # Criando os alunos
    aluno1 = Aluno(matricula="001", nome="Luciano", nota1=3.6, nota2=4.5, trabalho=6)
    aluno2 = Aluno(matricula="002", nome="Jayden", nota1=9, nota2=8.5, trabalho=9)
    aluno3 = Aluno(matricula="003", nome="Judas", nota1=7.5, nota2=8.4, trabalho=6)

    calculadora = Media()
    controller = CalculadorMedia()

    alunos = [aluno1, aluno2, aluno3]

    for aluno in alunos:
        media = calculadora.media(aluno)
        quanto_falta = calculadora.final(aluno)

        print(f"Aluno: {aluno.nome}")
        print(f"Média: {media:.2f}")
        print(f"Precisa na final: {quanto_falta:.2f}")
        print("-" * 30)


if __name__ == "__main__":
    main()