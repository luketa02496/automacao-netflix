# 🖥️ Script de Automação Netflix + Desligamento Programado

Este script automatiza o processo de **pular introduções, recaps e próximos episódios** na Netflix, além de permitir **programar o desligamento automático do computador** em um horário definido pelo usuário.

O programa também cria e atualiza automaticamente um **arquivo de histórico (`historico.txt`)**, registrando todas as ações realizadas (horário e tipo de ação).

---

## ⚙️ Funcionalidades

✅ Pular automaticamente:
- Introduções (abertura)
- Recaps (resumo anterior)
- Próximo episódio

✅ Programar o horário de desligamento do PC.

✅ Menu de configurações acessível a qualquer momento pressionando **Enter**:
- Reprogramar o desligamento
- Cancelar o desligamento
- Trocar o idioma (Português/Inglês)
- Encerrar o programa
- Cancelar ação

✅ Detecção automática de imagens (dependendo do idioma).

✅ Registro completo das ações no arquivo `historico.txt`.

---

## 🗂️ Estrutura de Pastas

```
📂 pasta_do_projeto/
│
├── main.py                     # Script principal
├── imagens/                    # Pasta contendo as imagens usadas pelo PyAutoGUI
│   ├── pular_intro.png
│   ├── pular_ep.png
│   ├── pular_recap.png
│   ├── skip_intro.png
│   ├── next_ep.png
│   └── skip_recap.png
│
├── idioma.txt                  # Arquivo criado automaticamente com o idioma do usuário
├── historico.txt               # Histórico das ações realizadas
└── README.md                   # Este arquivo
```

---

## 🧩 Requisitos

Antes de executar o script, instale as dependências necessárias:

```bash
pip install pyautogui
pip install pillow
```

> 💡 **Dica:** O `pyautogui` depende do `pillow` para o reconhecimento das imagens na tela.

---

## ▶️ Como Executar o Script (.py)

1. Certifique-se de que a pasta `imagens` está no **mesmo diretório** do arquivo `.py`.
2. Execute o script no terminal:

```bash
python automatizacao_netflix.py
```

3. Siga as instruções exibidas no console.

---

## 🧱 Gerando o Arquivo Executável (.exe)

Para gerar o `.exe` e poder usar o programa **sem precisar do Python instalado**, utilize o **PyInstaller**:

### Instalar o PyInstaller:
```bash
pip install pyinstaller
```

### Gerar o executável:
No terminal, dentro da pasta do projeto, execute:

```bash
pyinstaller --onefile --add-data "imagens;imagens" automatizacao_netflix.py
```

📌 **Explicação:**
- `--onefile` → Cria um único arquivo `.exe`.
- `--add-data "imagens;imagens"` → Inclui a pasta `imagens` dentro do executável.
  - No Windows, use `;` entre os caminhos.
  - No Linux/Mac, use `:`.

O executável será criado dentro da pasta:
```
dist/main.exe
```

---

## 📄 Arquivos Criados Automaticamente

- **`idioma.txt`** → Armazena o idioma selecionado (1 para Português, 2 para Inglês).
- **`historico.txt`** → Guarda todas as ações realizadas com data e hora.

---

## 🔒 Observações Importantes

- As imagens da pasta `imagens` **devem estar exatamente nomeadas** como no script.
- O programa **precisa ser executado com a Netflix aberta**.
- Caso alguma imagem não seja encontrada, o programa exibirá uma mensagem de erro e encerrará.
Este projeto é de uso pessoal e educacional.  
Sinta-se à vontade para modificar e estudar o código.
