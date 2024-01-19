# English Version
 
This project was developed for the subject 'Laboratório de IACD' by the students [André Sousa](https://github.com/anfisou), [António Cardoso](https://github.com/ToniCardosooo), [Antónia Brito](https://github.com/Nia3324) and [Paulo Silva](https://github.com/WrekingPanda).

In this project, our work which takes focus on recreating an adversarial model inspirated on DeepMind's AlphaZero capable of learning to play the games of Go and Ataxx.

To achieve this, we created a machine learning model based on the AlphaZero aproach, making use of a Convolutional Neural Network and a Monte Carlo Tree Search algorythm.

On top of that we implemented some features of our own, such as:
- Multiple games can be played in parallel
- A model that can play on different sized boards
- Data Augmentation by applying transformations to board states
- Introduction of noise to mitigate overfitting

The final work is distribuited on theese files:
- aMCTS_parallel.py: which implements the MCTS
- az_parallel2.py: containing the AlphaZero class
- ataxx.py and go.py: that implement the rules of the games
- graphics.py: to display the pygame interface
- play_AI.py: to play against a trained model
- ataxx4x4.py, ataxx5x5.py, ataxx6x6.py, ataxxflex.py, go7x7.py and go9x9.py: to train each model

If you wish to play against your models, you can do it by changing the game characteristics, the model characteristics and the model path in play_AI.py and running it.

# Versão Portuguesa

Este projeto foi desenvolvido no âmbito da unidade curricular 'Laboratório de IACD' pelos alunos [André Sousa](https://github.com/anfisou), [António Cardoso](https://github.com/ToniCardosooo), [Antónia Brito](https://github.com/Nia3324) e [Paulo Silva](https://github.com/WrekingPanda).


Neste projeto, o nosso trabalho concentra-se em recriar um modelo adversarial inspirado no AlphaZero da DeepMind, capaz de aprender a jogar os jogos de Go e Ataxx.

Para alcançar isso, criamos um modelo baseado na abordagem AlphaZero, fazendo uso de uma Rede Neural Convolucional e um algoritmo de Busca em Árvore de Monte Carlo.

Além disso, implementamos algumas características próprias, tais como:

- Múltiplos jogos podem ser jogados em paralelo
- Um modelo que pode jogar em tabuleiros de diferentes tamanhos
- Data Augmentation aplicando transformações aos estados do tabuleiro
- Introdução de ruído para combater overfitting

O trabalho final está distribuido pelos seguintes ficheiros:
- aMCTS_parallel.py: que implementa a MCTS
- az_parallel2.py: que contém a classe AlphaZero
- ataxx.py e go.py: implementando as regras dos jogos
- graphics.py: para mostrar o jogo numa interface gráfica pygam
- play_AI.py: para jogar contra um modelo treinado
- ataxx4x4.py, ataxx5x5.py, ataxx6x6.py, ataxxflex.py, go7x7.py e go9x9.py: para treinar cada modelo

Para jogar contra os modelos, é necessário alterar as caraterísticas do jogo, do modelo e o caminho para o modelo em play_AI.py e correr esse ficheiro.
