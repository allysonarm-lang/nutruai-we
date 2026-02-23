# NutriAI - Instruções para Agentes IA

## Visão Geral
**NutriAI** é um sistema CLI de monitoramento nutricional em Python que fornece cálculos de saúde (IMC, gasto calórico, macronutrientes) e análise de evolução de peso com previsões usando regressão linear.

## Arquitetura

### Estrutura de Projeto
```
nutruai-we/
├── nutruai/           # Código principal
│  ├── __init__.py     # Exports públicas
│  ├── calculator.py   # Cálculos nutricionais
│  ├── health.py       # Previsões e histórico
│  └── cli.py          # Interface de linha de comando
├── tests/             # Testes unitários
├── docs/              # Documentação
└── requirements.txt   # Dependências
```

### Componentes Principais

1. **`calculator.Calculator`** - Cálculos estáticos
   - `calcular_imc()`: Índice de Massa Corporal
   - `calcular_gasto_calorico()`: TMB e TDEE (Mifflin-St Jeor)
   - `distribuir_macronutrientes()`: Divisão por tipo de dieta

2. **`health.HealthPredictor`** - Análise de série temporal
   - Carrega/salva histórico em CSV
   - Treina modelo LinearRegression em peso vs dias
   - Gera gráficos com matplotlib

3. **`cli.NutriAICLI`** - Menu interativo
   - 7 operações principais
   - Coleta entrada do usuário
   - Exibe resultados formatados

## Padrões e Convenções

### Entrada de Dados
- Sempre usar `float(input())` ou `int(input())` com bloco try/except
- Validar tipo de dado antes de processar
- Aceitar siglas em maiúscula: `sexo.upper()`

### Dados de Peso
- Histórico armazenado em `historico.csv` (3 colunas: data, peso, opcional)
- Datas em formato ISO: `"YYYY-MM-DD"`
- Conversão com `pd.to_datetime()`

### Modelos de ML
- Usar `sklearn.linear_model.LinearRegression` para previsões
- Sempre converter datas em número de dias desde mínimo: `(df["data"] - df["data"].min()).dt.days`
- X precisa ser reshape(-1, 1) para sklearn

### Estilo de Código
- Type hints em funções
- Docstrings em estilo Google
- Emojis em prints (IMC=📊, Previsão=🔮, Erro=❌)

## Fluxo de Desenvolvimento

### Configurar Ambiente Local
```bash
python -m venv venv
source venv/bin/activate  # ou: venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

### Executar Aplicação
```bash
cd nutruai
python cli.py
```

### Executar Testes
```bash
python tests/test_calculator.py
```

### Adicionar Nova Funcionalidade
1. Implementar função em `calculator.py` ou `health.py`
2. Adicionar case no menu `menu_principal()` da CLI
3. Escrever teste em `tests/test_*.py`
4. Atualizar `README.md`

## Dependências
- **pandas**: Manipulação de dados e CSV
- **matplotlib**: Visualização de gráficos
- **scikit-learn**: Modelos de regressão
- **numpy**: Operações numéricas

## Implantação Online

### Opção 1: Documentação no GitHub Pages
- Site estático em `/docs` com instruções de uso
- GitHub Actions pode automatizar build de docs

### Opção 2: Tornar um Pacote PyPI
```bash
pip install nutruai
nutruai-cli  # executa a CLI globalmente
```

### Opção 3: Web API (Flask/FastAPI)
- Se quiser interface web, envolver calculadoras em endpoints REST
- Fazer deploy em Heroku, Railway ou PythonAnywhere

## Tópicos-Chave para IA
- 🧮 Fórmulas médicas usam padrões fixos (Mifflin-St Jeor, Harris-Benedict)
- 📊 Regressão linear é bom para tendência; usar mais modelos avançados com cuidado
- 📁 Persistência é via CSV simples (sem database)
- 🎯 Dietas: balanceada (30/50/20), lowcarb (30/20/50), highprotein (40/40/20)
- 🔄 Menu CLI é sequencial; para concorrência, migrar para CLI assíncrona (click + asyncio)

## Referências Rápidas
- Fórmula TMB (Mifflin): `(10*peso) + (6.25*altura_cm) - (5*idade) + 5/−161`
- 1g proteína/carboidrato = 4 calorias
- 1g gordura = 9 calorias
- IMC < 18.5 → Abaixo / 18.5-25 → Normal / 25-30 → Sobrepeso / 30+ → Obesidade
