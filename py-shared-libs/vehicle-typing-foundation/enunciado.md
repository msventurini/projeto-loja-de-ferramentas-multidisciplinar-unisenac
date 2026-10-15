

# Sistema de Estacionamento Inteligente

### Descrição:

 Utilizando os conceitos de Orientação a Objetos, implemente um sistema para gerenciar um estacionamento. O sistema deve permitir cadastrar veículos, controlar vagas, calcular tarifas de acordo com o tipo de veículo e manter um histórico de entradas e saídas.

## Requisitos obrigatórios:

- Criar classes para: 
    - Veiculo; 
    - Carro; 
    - Moto; 
    - Caminhao; 
    - Vaga;
    - Estacionamento.

- Implementar herança entre Veiculo e suas subclasses.
- Implementar polimorfismo no método calcular_tarifa().
- Garantir encapsulamento em atributos.
- Usar composição: Estacionamento contém várias Vagas.
- Lançar exceções ao tentar estacionar em vaga ocupada.
- Implementar persistência simples (salvar histórico em arquivo JSON).

Requisitos opcionais (desafio):

Criar vagas especiais (deficientes, elétricos, VIP).
Implementar relatórios de ocupação e faturamento.
Criar interface de texto para interação com o usuário.


### Casos de Uso

- Cadastrar veículo: Usuário informa placa e modelo, sistema cria objeto Carro, Moto ou Caminhao.
- Estacionar veículo: Usuário informa placa e vaga, sistema ocupa a vaga se disponível.
- Retirar veículo: Usuário informa placa, sistema libera a vaga e calcula tarifa.
- Gerar relatório: Sistema mostra vagas ocupadas, vagas livres e faturamento total.

### Regras de Negócio

- Cada vaga só pode conter um veículo por vez.
- Tarifas variam por tipo de veículo:
- Carro: R$ 10/hora
- Moto: R$ 5/hora
- Caminhão: R$ 20/hora
- Se tentar estacionar em vaga ocupada, lançar exceção.
- Histórico deve registrar placa, tipo de veículo, horário de entrada e saída, valor pago.