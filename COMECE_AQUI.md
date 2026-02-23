# COMEÇAR AQUI 🚀

Este guia rápido mostra como começar a usar o NutriAI após clonar o repositório.

## 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/allysonarm-lang/nutruai-we.git
cd nutruai-we
```

## 2️⃣ Criar Ambiente Virtual

### Linux / macOS
```bash
python -m venv venv
source venv/bin/activate
```

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

## 3️⃣ Instalar Dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4️⃣ Executar Testes

```bash
python tests/test_calculator.py
```

✅ Se tudo passar, o ambiente está configurado!

## 5️⃣ Usar a Aplicação

### CLI Interativa
```bash
cd nutruai
python cli.py
```

### Como Biblioteca Python
```python
from nutruai.calculator import Calculator

calc = Calculator()
resultado = calc.calcular_imc(70, 1.75)
print(f"IMC: {resultado['imc']}")
print(f"Classificação: {resultado['classificacao']}")
```

## 📦 Alternativa: Instalar como Pacote

```bash
pip install -e .
```

Depois use em qualquer lugar:
```bash
nutruai
```

---

## 🌐 Deixar Online

Veja [HOSPEDAGEM.md](./HOSPEDAGEM.md) para opções de:
- 📄 GitHub Pages
- 📦 PyPI Package
- 🌍 Web API (Railway/Render)
- 💾 Executável Standalone

---

## 📚 Documentação Completa

- [README.md](./README.md) - Overview completo
- [.github/copilot-instructions.md](./.github/copilot-instructions.md) - Guia para agentes IA
- [HOSPEDAGEM.md](./HOSPEDAGEM.md) - Opções de deploy online

---

## 🐛 Encontrou um Bug?

Abra uma [issue no GitHub](https://github.com/allysonarm-lang/nutruai-we/issues)!
