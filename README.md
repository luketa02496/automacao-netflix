MARCELLA EU TE AMOOOOOOOOOOOOOO MUITOOOOOOOOOOOOOOOOOOOOOOO <3

# 📺 Automação Netflix — Skip Intro, Recap & Episódio + Desligamento Automático  

Este projeto automatiza ações repetitivas na Netflix usando **Python** e **PyAutoGUI**, como:
- Pular introduções 
- Pular recaps 
- Ir para o próximo episódio   
Além disso, permite **programar o desligamento automático do computador** em um horário específico.  

---

## 🧠 Funcionalidades principais

- 🕓 **Programar desligamento automático** do PC em uma hora definida.  
- 🎬 **Pular automaticamente** aberturas, recaps e episódios seguintes.  
- 🌐 **Compatível com múltiplos idiomas** (Português e Inglês).  
- 💾 **Registro de histórico** de ações em arquivo (`historico.txt`).  
- ⚙️ **Menu de configurações interativo** acessível durante a execução.  
- 🧩 **Autodetecção de diretórios** — funciona tanto no script `.py` quanto no executável `.exe`.

---

## 🗂️ Estrutura de Pastas

O projeto deve seguir esta estrutura:

```
📁 automatizacao_netflix
│
├── automatizacao_netflix.py
├── imagens/
│   ├── pular_intro.png
│   ├── pular_ep.png
│   ├── pular_recap.png
│   ├── skip_intro.png
│   ├── next_ep.png
│   └── skip_recap.png
├── idioma.txt           ← gerado automaticamente após a primeira execução
└── historico.txt        ← gerado automaticamente
```

> ⚠️ **A pasta `imagens` é obrigatória** e deve estar na mesma pasta do executável ou do script Python.

---

## 🧩 Requisitos

Antes de executar o script, é necessário ter:

- **Python 3.10+**
- As seguintes bibliotecas instaladas:
  ```bash
  pip install pyautogui
  pip install pyinstaller
  ```
> 💡 No Windows, você também pode precisar do módulo `pillow`:
> ```bash
> pip install pillow
> ```

---

## ▶️ Como usar o script

1. **Abra o script no terminal:**
   ```bash
   python automatizacao_netflix.py
   ```

2. O programa perguntará:
   ```
   Você deseja programar o PC para desligar? (S/N)
   ```

3. Em seguida:
   - Informe a hora no formato `0000` (exemplo: `2330` para 23:30h).
   - Escolha o idioma da sua Netflix (`1` para Português, `2` para Inglês).
   - Abra a Netflix e pressione **Enter** quando estiver pronto.

4. O script ficará em execução, monitorando a tela a cada 5 segundos e clicando automaticamente nos botões:
   - **Pular introdução**
   - **Pular recap**
   - **Próximo episódio**

5. Durante a execução, pressione **Enter** para acessar o **Menu de Configurações**:
   - `1` — Reprogramar desligamento  
   - `2` — Cancelar desligamento  
   - `3` — Trocar idioma  
   - `4` — Encerrar programa  
   - `5` — Cancelar ação e retornar  

---

## 🧱 Gerar executável (.exe)

Para criar um executável independente, use o **PyInstaller**.

1. No terminal, execute:
   ```bash
   pyinstaller --onefile --add-data "imagens;imagens" automatizacao_netflix.py
   ```

   > ⚙️ Explicação:
   > - `--onefile` → gera um único `.exe`.
   > - `--add-data "imagens;imagens"` → inclui a pasta `imagens` dentro do executável (Windows usa `;` — no Linux/Mac seria `:`).

2. O executável será criado em:
   ```
   dist/automatizacao_netflix.exe
   ```

3. Mova o `.exe` para uma pasta de sua preferência e **mantenha a pasta `imagens` no mesmo diretório** (caso tenha empacotado sem ela).

---

## 📄 Arquivos gerados automaticamente

| Arquivo | Descrição |
|----------|------------|
| `idioma.txt` | Guarda o idioma selecionado pelo usuário. |
| `historico.txt` | Registra todas as ações executadas e os horários. |

---

## 💬 Mensagens de log

Durante a execução, o programa exibirá:
- Confirmações das ações (ex: `"abertura pulada"`, `"episodio pulado"`).
- Instruções para acessar o menu de configurações.
- Informações de status a cada 10 minutos.

---

## 💡 Dicas de uso

- Execute o programa **com o navegador em tela cheia** para que o PyAutoGUI reconheça corretamente os botões.
- Certifique-se de que as imagens da pasta `imagens` **são capturas idênticas** aos botões exibidos na sua Netflix.
- Caso as imagens não sejam reconhecidas, você pode substituir os arquivos `.png` por novas capturas (mesmos nomes).

---

## ⚠️ Observações

- O script foi projetado para **Windows**, usando o comando `shutdown /s /f /t 3`.
- Para rodar no Linux ou macOS, substitua o comando dentro da função `desligar_pc()`:
  ```python
  os.system("shutdown now")  # Linux/macOS
  ```
- O programa depende da **posição e aparência** dos botões na tela. Pequenas variações visuais podem afetar a detecção.

