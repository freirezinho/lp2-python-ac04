'''
Saulo Santos Freire – RA: 1902635
Lucas Barbosa Lima de Souza Santos - RA: 1903921
'''
from history import Historico
from pacient import Paciente
from physician import Medico
from room import Quarto
from datetime import datetime


def main():

    # Instanciando os objetos
    print('\nPreparando o médico...\n')
    print('---------------------------------')
    medico_padrao = Medico(
        nome='César Thiago Mateus da Costa',
        rg='44.647.509-9',
        cpf='825.372.144-71',
        crm='123.1234.525.00',
        telefone='(71) 3975-3150',
        salario=5000,
        especialidades=['Cardiologista', 'Clínico Geral']
    )
    print('Médico preparado:')
    print(f'Nome: {medico_padrao.get_nome()}')
    print(f'CRM: {medico_padrao.get_crm()}')
    print(f'RG: {medico_padrao.get_rg()}')
    print(f'CPF: {medico_padrao.get_cpf()}')
    print(f'CRM: {medico_padrao.get_crm()}')
    print(f'Salario: {medico_padrao.get_salario()}')
    print(f'Especialidades: {medico_padrao.get_especialidade_principal()}')
    print('---------------------------------')
    # O médico já é designado ao paciente no momento de inicialização
    print('\nRegistrando paciente com o médico preparado anteriormente...\n')
    novo_paciente = Paciente(
        nome='Guilherme Yuri Lucas dos Santos',
        rg='27.824.347-2',
        cpf='350.666.559-64',
        endereco='Rua Ipecaetá, 756, Praia do Flamengo – Salvador, BA',
        telefone='(71) 3973-5446',
        data_nascimento='09/03/1964',
        responsavel=medico_padrao
    )
    print('---------------------------------')
    print('Paciente registrado:')
    print(f'Nome: {novo_paciente.get_nome()}')
    print(f'RG: {novo_paciente.get_rg()}')
    print(f'CPF: {novo_paciente.get_cpf()}')
    print(f'Endereço: {novo_paciente.get_endereco()}')
    print(f'Telefone: {novo_paciente.get_telefone()}')
    print(f'Data de Nascimento: {novo_paciente.get_data_nascimento()}')
    print(f'Responsável: {novo_paciente.get_responsavel().get_nome()}')
    print('---------------------------------')

    quarto_disponivel = Quarto(numero=10, andar=5)

    # Um quato é designado ao paciente, e ele é internado
    print(
        f'\nDesignando quarto....'
        f'{quarto_disponivel.get_numero()}'
        f'do andar número {quarto_disponivel.get_andar()} ao paciente...\n')
    novo_paciente.designar_quarto(quarto_disponivel)
    novo_paciente.internar_paciente(True)

    # Preparamos os dados do histórico
    print('Preparando dados do histórico...')
    hoje = str(datetime.now().date())
    horario_atual = str(datetime.now().time())
    observacao_a_escrever = 'O paciente chegou com taquicardia.'
    nome_medico = medico_padrao.get_nome()
    crm_medico = medico_padrao.get_crm()
    assinatura_medico = f'{nome_medico} | {crm_medico}'

    # Registramos o histórico ao paciente
    print('\nCriando registro no histórico...\n')
    novo_paciente.registrar_historico(
        data=hoje,
        horario=horario_atual,
        observacao=observacao_a_escrever,
        medico=assinatura_medico)
    print('\nBuscando todos os registros do histórico...\n')
    print('--------------------------')
    print('Registros do Histórico')
    novo_paciente.get_historico()


main()
