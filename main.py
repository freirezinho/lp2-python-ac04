"""
Saulo Santos Freire – RA: 1902635
Lucas Barbosa Lima de Souza Santos - RA: 1903921
"""
from history import Historico
from pacient import Paciente
from physician import Medico
from room import Quarto
from datetime import datetime


def main():

    # Instanciando os objetos

    medico_padrao = Medico(
        nome="César Thiago Mateus da Costa",
        rg="44.647.509-9",
        cpf="825.372.144-71",
        crm="123.1234.525.00",
        telefone="(71) 3975-3150",
        salario=5000,
        especialidades=["cardiologista", "clinico geral"]
    )
    # O médico já é designado ao paciente no momento de inicialização
    novo_paciente = Paciente(
        nome="Guilherme Yuri Lucas dos Santos",
        rg="27.824.347-2",
        cpf="350.666.559-64",
        endereco="Rua Ipecaetá, 756, Praia do Flamengo – Salvador, BA",
        telefone="(71) 3973-5446",
        data_nascimento="09/03/1964",
        responsavel=medico_padrao
    )

    quarto_disponivel = Quarto(numero=10, andar=5)

    # Um quato é designado ao paciente, e ele é internado

    novo_paciente.designar_quarto(quarto_disponivel)
    novo_paciente.internar_paciente(True)

    # Preparamos os dados do histórico

    hoje = str(datetime.now().date())
    horario_atual = str(datetime.now().time())
    observacao_a_escrever = 'O paciente chegou com taquicardia.'
    assinatura_medico = f'{medico_padrao.get_nome()} | {medico_padrao.get_crm()}'

    # Registramos o histórico ao paciente

    novo_paciente.registrar_historico(
        data=hoje,
        horario=horario_atual,
        observacao=observacao_a_escrever,
        medico=assinatura_medico)
    novo_paciente.get_historico()


main()
