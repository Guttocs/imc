def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return (
            f"IMC: {imc:.2f} - Baixo peso.\n"
            "Recomendado procurar um médico para avaliação criteriosa do resultado. "
            "Pode indicar um estado de consumo do organismo, com poucas reservas e riscos associados."
        )
    elif 18.5 <= imc <= 24.9:
        return (
            f"IMC: {imc:.2f} - Peso adequado.\n"
            "Tudo indica que está tudo bem, mas é importante avaliar outros parâmetros da composição corporal. "
            "Algumas pessoas apresentam IMC normal, mas têm circunferência abdominal e/ou massa gorda acima do ideal."
        )
    elif 25.0 <= imc <= 29.9:
        return (
            f"IMC: {imc:.2f} - Sobrepeso.\n"
            "Associado ao risco de doenças como diabetes e hipertensão. "
            "Consulte um médico e reveja hábitos. Avalie também a circunferência abdominal."
        )
    elif 30.0 <= imc <= 34.9:
        return (
            f"IMC: {imc:.2f} - Obesidade Grau I.\n"
            "Importante buscar orientação médica e nutricional, mesmo que exames estejam normais."
        )
    elif 35.0 <= imc <= 39.9:
        return (
            f"IMC: {imc:.2f} - Obesidade Grau II.\n"
            "Quadro mais evoluído. Não adie a procura por orientação médica e nutricional."
        )
    else:  # IMC >= 40.0
        return (
            f"IMC: {imc:.2f} - Obesidade Grau III.\n"
            "Maior risco de doenças associadas. Procure ajuda médica com urgência."
        )

try:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = calcular_imc(peso, altura)
    resultado = classificar_imc(imc)
    print("\n" + resultado)

except ValueError:
    print("Por favor, digite valores numéricos válidos para peso e altura.")
