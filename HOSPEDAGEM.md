# 🌐 Guia de Hospedagem Online - NutriAI

Este documento descreve as opções para deixar a aplicação NutriAI disponível online.

---

## 📋 Resumo das Opções

| Opção | Tipo | Custo | Facilidade | Ideal Para |
|-------|------|-------|-----------|-----------|
| **GitHub Pages** | Site Estático | Grátis | ⭐⭐⭐ | Documentação |
| **PyPI Package** | Instalação Global | Grátis | ⭐⭐⭐⭐ | Distribuição via pip |
| **Railway/Render** | PaaS | Grátis/Pago | ⭐⭐⭐⭐ | Web app + API |
| **Executável** | Standalone | Grátis | ⭐⭐⭐ | Desktop app |

---

## Opção 1️⃣: GitHub Pages (Documentação)

### Descrição
Publicar site estático com documentação, guias e links para usar a CLI local.

### Como Fazer

#### 1.1 - Criar pasta `docs` com conteúdo HTML

```bash
mkdir -p docs
```

#### 1.2 - Criar `docs/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NutriAI - Sistema de Nutrição</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background, #f5f5f5;
        }
        h1 { color: #2ecc71; }
        .highlight { background: #fffacd; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>🧠 NutriAI - Monitoramento Nutricional</h1>
    <p>Sistema inteligente para cálculos de saúde e nutrição.</p>
    
    <h2>Instalação Rápida</h2>
    <pre>pip install -e .</pre>
    
    <h2>Usar CLI</h2>
    <pre>python nutruai/cli.py</pre>
    
    <h2>Documentação Completa</h2>
    <p>Veja o <a href="https://github.com/allysonarm-lang/nutruai-we">repositório no GitHub</a></p>
</body>
</html>
```

#### 1.3 - Ativar GitHub Pages

1. Ir em **Settings** → **Pages**
2. Em "Source", selecionar **main branch** → **/docs folder**
3. Salvar

📍 **Site estará em**: `https://allysonarm-lang.github.io/nutruai-we`

---

## Opção 2️⃣: Publicar no PyPI (Instalação Global)

### Descrição
Permitir instalação global com `pip install nutruai`

### Como Fazer

#### 2.1 - Criar `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name="nutruai",
    version="0.1.0",
    author="allysonarm-lang",
    author_email="seu-email@example.com",
    description="Sistema inteligente de monitoramento nutricional",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/allysonarm-lang/nutruai-we",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0",
        "matplotlib>=3.5",
        "scikit-learn>=1.0",
        "numpy>=1.20",
    ],
    entry_points={
        "console_scripts": [
            "nutruai=nutruai.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
```

#### 2.2 - Criar `MANIFEST.in`

```
include README.md
include requirements.txt
recursive-include nutruai *.py
```

#### 2.3 - Build e Upload

```bash
# Instalar ferramentas
pip install build twine

# Criar distribuição
python -m build

# Fazer upload (requer conta PyPI)
python -m twine upload dist/*
```

📍 **Após publicado**: `pip install nutruai`

---

## Opção 3️⃣: Web API com Flask/FastAPI

### Descrição
Transformar em REST API com interface web, hospedado em nuvem.

#### 3.1 - Criar `app.py`

```python
from flask import Flask, request, jsonify
from nutruai.calculator import Calculator
from nutruai.health import HealthPredictor

app = Flask(__name__)
calc = Calculator()
predictor = HealthPredictor('historico.csv')

@app.route('/api/imc', methods=['POST'])
def api_imc():
    data = request.json
    result = calc.calcular_imc(data['peso'], data['altura'])
    return jsonify(result)

@app.route('/api/gasto-calorico', methods=['POST'])
def api_gasto():
    data = request.json
    result = calc.calcular_gasto_calorico(
        data['peso'],
        data['altura'],
        data['idade'],
        data['sexo'],
        data['atividade']
    )
    return jsonify(result)

@app.route('/api/macros', methods=['POST'])
def api_macros():
    data = request.json
    result = calc.distribuir_macronutrientes(
        data['calorias'],
        data.get('dieta', 'balanceada')
    )
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
```

#### 3.2 - Deploy em Railway

```bash
# Instalar CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway init
railway up
```

📍 **URL da API**: `https://seu-app-railway.up.railway.app/api/imc`

---

## Opção 4️⃣: Executável Standalone

### Descrição
Criar `.exe` (Windows) ou `.app` (macOS) para uso desktop.

#### 4.1 - Instalar PyInstaller

```bash
pip install pyinstaller
```

#### 4.2 - Gerar Executável

```bash
pyinstaller --onefile --windowed nutruai/cli.py
```

#### 4.3 - Distribuir

O executável estará em `dist/cli.exe`

Você pode:
- Hospedar em GitHub Releases
- Disponibilizar em um site
- Distribuir diretamente aos usuários

---

## ✅ Recomendação

Para **NutriAI**, a melhor estratégia é **combinação de 2 + 1**:

1. **Publicar no PyPI** → `pip install nutruai` (facilita instalação)
2. **GitHub Pages** → Documentação e tutorial
3. **Opcional**: Web API em Railway para usuários sem Python

```bash
# Fluxo recomendado de uso
pip install nutruai
nutruai  # CLI executável
```

---

## 🔧 Próximos Passos

- [ ] Criar `setup.py` para PyPI
- [ ] Configurar GitHub Pages
- [ ] Escrever documentação em `/docs`
- [ ] Criar CI/CD com GitHub Actions
- [ ] Fazer upload para PyPI (versão 0.1.0)

---

**Dúvidas?** Abra uma [issue no GitHub](https://github.com/allysonarm-lang/nutruai-we/issues)
