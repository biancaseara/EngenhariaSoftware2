
# **Documento de Especificação Funcional (DEF)**

---

## 0. Visão geral do projeto

* **Nome do Software**: Grey Roots
* **Versão:** 1.0
* **Data:** 05/11/2025
* **Autor(es):** Ayla Maria Araujo Berbert, Bianca Seara Pereira e Celeste Moraes Silva.


---

## 1. Introdução

### 1.1 Propósito

Este documento descreve os requisitos funcionais e não funcionais do jogo Grey Roots. Ele detalha como o jogador irá interagir com o sistema, o funcionamento interno da lógica narrativa e as condições de progresso e finalização do jogo.

### 1.2 Escopo

O jogo é uma história orientada a narrativo e baseado em escolhas. O jogador percorre um mundo ficcional, interagindo atraves da coleta e uso de itens, toma decisões que afetam a trama, cuja trajetória se altera conforme suas decisões. O jogo:

* Registra nome e signo do jogador;
* Atribui uma planta espiritual associada ao signo;
* Apresenta narrativa visual e textual;
* Permite escolhas com consequências;
* Coleta e uso de itens;
* Execução de eventos QTE;
* Possui múltiplos finais.


### 1.3 Definições, acrônimos e abreviações

| Termo   | Definição           |
| --------| --------------------|
| QTE     | Quick Time Event    |

                         

---

## 2. Descrição Geral

### 2.1 Perspectiva do Produto

O produto é um aplicativo local em Python que usa PyGame para interface gráfica e entrada do jogador.

### 2.2 Funções do Produto

* Entrada de nome e signo;
* Atribuição de uma planta espiritual correspondente ao signo;
* Navegação por cenas e escolhas narrativas;
* Coleta, exibição e uso de itens;
* Execução de eventos QTE;
* Alterar o desfecho conforme decisões.



### 2.3 Características dos Usuários

Jogadores com interesse em jogos narrativos.

### 2.4 Restrições

* Necessário Python 3.8+ e PyGame instalados;
* Execução em sistemas desktop.
* Interação exclusivamente via teclado.


### 2.5 Suposições e Dependências

| Bibliotecas | Função            |
| ----------- | ----------------- |
| Python 3.8+ | Execução do jogo  |
| PyGame      | Interface gráfica |


---

## 3. Requisitos Funcionais (RF)

| Código | Descrição                                                                      |
| ------ | ------------------------------------------------------------------------------ |
| RF001  | O sistema deve solicitar e armazenar o nome do jogador.                        |
| RF002  | O sistema deve solicitar e armazenar o signo do jogador.                       |
| RF003  | O sistema deve associar ao jogador uma planta baseada no signo.                |
| RF004  | O sistema deve exibir textos narrativos e imagens referentes às cenas.         |
| RF005  | O sistema deve permitir que o jogador selecione opções numeradas para avançar. |
| RF006  | O sistema deve permitir adicionar e consultar itens coletados.                 |
| RF007  | O sistema deve registrar decisões e alterar cenas futuras com base nelas.      |
| RF008  | O sistema deve apresentar eventos de reação rápida em determinados pontos.     |
| RF009  | O sistema deve apresentar finais distintos conforme decisões registradas.      |



---

## 4. Requisitos Não Funcionais (RNF)

| Código | Requisito        | Descrição                                                                    |
| ------ | ---------------- | ---------------------------------------------------------------------------- |
| RNF001 | Desempenho       | A transição entre cenas deve ocorrer em até 1 segundo.                       |
| RNF002 | Usabilidade      | Interface textual clara e legível.                                           |
| RNF003 | Confiabilidade   | O jogo deve operar de forma estável, sem interrupções ou falhas inesperadas. | 
---



## 7. Casos de Uso

### 7.1. Iniciar jogo

O jogador executa o programa.
O sistema exibe a tela inicial.
O jogador seleciona a opção “Iniciar”.
O sistema inicia a narrativa.


7.2 Configurar personagem

O sistema solicita nome e signo do personagem.
O jogador informa os dados.
O sistema registra as informações e personaliza o início da história.

7.3. Explorar ambiente
O jogador escolhe navegar pelos cenários e áreas disponíveis.
O sistema muda a tela ou descrição para a nova sala ou local.
O jogador pode continuar explorando ou retornar.

7.4. Interagir com objetos
O jogador seleciona um objeto ou elemento do ambiente (ex.: gavetas, lampião, mesa).
O sistema apresenta o resultado da interação (abrir, acender, observar, pegar).
O jogo continua com base nessa interação.

7.5. Coletar itens

O jogador encontra um item no ambiente.
O jogador escolhe coletar.
O sistema adiciona o item ao inventário do personagem.


7.6. Realizar QTE (Quick Time Event)

O sistema apresenta um evento que exige ação rápida (ex.: fuga, desviar, empurrar).
O sistema exibe uma tecla ou sequência para o jogador pressionar rapidamente.
O jogador tenta executar a ação no tempo limite.
Se acertar: o sistema continua a narrativa com sucesso.
Se falhar: o sistema segue para uma consequência negativa ou alternativa.

7.7 Tomar decisões

O jogador chega em um ponto da história com múltiplas escolhas.
O sistema apresenta opções (ex.: negociar, roubar, ajudar, ignorar).
O jogador seleciona uma das alternativas.
O sistema avança a narrativa com base na decisão tomada.

7.8 Finalizar / Sair do Jogo

O jogador escolhe a opção “Sair”.
O sistema encerra a execução do jogo de forma segura.
---
