# 🔐 Ciphers

Uma coleção de **cifras clássicas de substituição** implementadas em Python.

O projeto foi desenvolvido como parte dos meus estudos de **Python** durante minha graduação em **Análise e Desenvolvimento de Sistemas**, com foco na implementação dos algoritmos, organização do código e aplicação de conceitos de programação.

## ✨ Funcionalidades

Atualmente, o projeto conta com três algoritmos de criptografia:

* **Caesar Cipher** — deslocamento das letras do alfabeto
* **Atbash Cipher** — substituição de cada letra pela posição correspondente no alfabeto invertido
* **Vigenère Cipher** — cifra polialfabética baseada em uma palavra-chave

O programa possui um menu interativo que permite selecionar o algoritmo e realizar operações de **criptografia e descriptografia**.

## 🔑 Cifras implementadas

### Caesar Cipher

A cifra de César desloca cada letra do texto por uma quantidade determinada de posições no alfabeto.

Por exemplo, com deslocamento `3`:

```text
A → D
B → E
C → F
```

Exemplo:

```text
HELLO
```

com deslocamento `3`:

```text
KHOOR
```

A descriptografia utiliza o deslocamento inverso.

---

### Atbash Cipher

A cifra Atbash utiliza o alfabeto invertido para realizar a substituição:

```text
A ↔ Z
B ↔ Y
C ↔ X
```

Exemplo:

```text
HELLO
```

resulta em:

```text
SVOOL
```

Como a transformação é simétrica, o mesmo algoritmo pode ser utilizado para criptografar e descriptografar.

---

### Vigenère Cipher

A cifra de Vigenère utiliza uma **palavra-chave** para determinar diferentes deslocamentos ao longo do texto.

Por exemplo, utilizando a chave:

```text
KEY
```

cada letra da chave determina o deslocamento utilizado para a letra correspondente da mensagem.

Diferentemente da cifra de César, o deslocamento não é necessariamente o mesmo para todo o texto.

## 🛠️ Tecnologias

* **Python 3**
* Biblioteca padrão do Python

O projeto não depende de bibliotecas externas para executar os algoritmos de criptografia.

## 📁 Estrutura do projeto

```text
ciphers/
│
├── algorithms/
│   └── ciphers.py
│
├── utils/
│   └── validation.py
│
├── main.py
├── README.md
└── .gitignore
```

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/ciphers.git
```

Entre na pasta do projeto:

```bash
cd ciphers
```

Execute o programa:

```bash
python main.py
```

O menu principal permite escolher a cifra e a operação desejada.

## 🔎 Validação de entrada

O projeto possui funções de validação para controlar os dados fornecidos pelo usuário.

Entre os dados validados estão:

* Textos utilizados nas mensagens
* Valores inteiros
* Intervalos permitidos para os deslocamentos
* Chaves utilizadas pela cifra de Vigenère

A lógica de validação foi separada do restante do programa para manter uma melhor organização do código.

## 🧠 Conceitos praticados

O desenvolvimento do projeto permite praticar diversos conceitos fundamentais de Python:

* Funções
* Módulos e imports
* Listas e strings
* Loops
* Condicionais
* Manipulação de caracteres
* `ord()` e `chr()`
* Operador módulo `%`
* Validação de dados
* Organização de projetos em múltiplos arquivos
* Reutilização de funções
* Separação de responsabilidades

## ⚠️ Observação

As cifras implementadas neste projeto são **algoritmos históricos de criptografia** e não devem ser utilizadas para proteger informações reais.

Cifras como César, Atbash e Vigenère podem ser quebradas com técnicas relativamente simples e têm finalidade principalmente **educacional**.

## 📜 Licença

Este projeto foi desenvolvido para fins educacionais e de estudo.
