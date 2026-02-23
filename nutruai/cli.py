"""Interface de linha de comando (CLI) para NutriAI."""

import sys
from calculator import Calculator
from health import HealthPredictor


class NutriAICLI:
    """Interface CLI para interagir com NutriAI."""

    def __init__(self):
        self.calc = Calculator()
        self.health = HealthPredictor()

    def menu_principal(self):
        """Exibe e processa menu principal."""
        while True:
            print("\n" + "="*50)
            print("🧠 NutriAI - Sistema de Monitoramento Nutricional")
            print("="*50)
            print("1. Calcular IMC")
            print("2. Calcular Gasto Calórico")
            print("3. Distribuir Macronutrientes")
            print("4. Ver Histórico de Peso")
            print("5. Adicionar Peso")
            print("6. Previsão de Peso Futuro")
            print("7. Plotar Gráfico")
            print("0. Sair")
            print("="*50)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.calcular_imc()
            elif opcao == "2":
                self.calcular_gasto_calorico()
            elif opcao == "3":
                self.distribuir_macronutrientes()
            elif opcao == "4":
                self.ver_historico()
            elif opcao == "5":
                self.adicionar_peso()
            elif opcao == "6":
                self.previsao_peso()
            elif opcao == "7":
                self.plotar_grafico()
            elif opcao == "0":
                print("Até logo! 👋")
                break
            else:
                print("Opção inválida!")

    def calcular_imc(self):
        """Calcula IMC interativamente."""
        try:
            peso = float(input("Peso (kg): "))
            altura = float(input("Altura (m): "))
            resultado = self.calc.calcular_imc(peso, altura)
            print(f"\n📊 IMC: {resultado['imc']}")
            print(f"Classificação: {resultado['classificacao']}")
        except ValueError:
            print("❌ Entrada inválida!")

    def calcular_gasto_calorico(self):
        """Calcula gasto calórico interativamente."""
        try:
            peso = float(input("Peso (kg): "))
            altura = float(input("Altura (cm): "))
            idade = int(input("Idade (anos): "))
            sexo = input("Sexo (M/F): ").strip().upper()
            print("\nNível de atividade:")
            print("1.2 - Sedentário")
            print("1.375 - Pouco ativo")
            print("1.55 - Moderadamente ativo")
            print("1.725 - Muito ativo")
            print("1.9 - Extremamente ativo")
            atividade = float(input("Escolha: "))
            
            resultado = self.calc.calcular_gasto_calorico(peso, altura, idade, sexo, atividade)
            print(f"\n📊 TMB: {resultado['tmb']} calorias")
            print(f"TDEE: {resultado['tdee']} calorias/dia")
        except ValueError:
            print("❌ Entrada inválida!")

    def distribuir_macronutrientes(self):
        """Distribui macronutrientes interativamente."""
        try:
            calorias = float(input("Total de calorias diárias: "))
            print("\nTipo de dieta:")
            print("1. Balanceada (30% proteína, 50% carboidrato, 20% gordura)")
            print("2. Low-Carb (30% proteína, 20% carboidrato, 50% gordura)")
            print("3. High-Protein (40% proteína, 40% carboidrato, 20% gordura)")
            dieta_map = {"1": "balanceada", "2": "lowcarb", "3": "highprotein"}
            dieta = dieta_map.get(input("Escolha: "), "balanceada")
            
            resultado = self.calc.distribuir_macronutrientes(calorias, dieta)
            print(f"\n🥗 Proteína: {resultado['proteina_g']}g")
            print(f"🌾 Carboidrato: {resultado['carboidrato_g']}g")
            print(f"🧈 Gordura: {resultado['gordura_g']}g")
        except ValueError:
            print("❌ Entrada inválida!")

    def ver_historico(self):
        """Exibe histórico de peso."""
        self.health.carregar_dados()
        if self.health.df is not None and not self.health.df.empty:
            print("\n📈 Histórico de Peso:")
            print(self.health.df.to_string(index=False))
        else:
            print("Nenhum registro encontrado.")

    def adicionar_peso(self):
        """Adiciona novo registro de peso."""
        try:
            self.health.carregar_dados()
            data = input("Data (YYYY-MM-DD): ")
            peso = float(input("Peso (kg): "))
            self.health.adicionar_peso(data, peso)
            print("✅ Registro adicionado!")
        except ValueError:
            print("❌ Entrada inválida!")

    def previsao_peso(self):
        """Exibe previsão de peso futuro."""
        self.health.carregar_dados()
        dias = int(input("Quantos dias para prever? (padrão: 30): ") or "30")
        resultado = self.health.prever_peso_futuro(dias)
        
        if "erro" in resultado:
            print(f"❌ {resultado['erro']}")
        else:
            print(f"\n🔮 Previsão para {resultado['dias']} dias:")
            print(f"Peso atual: {resultado['peso_atual']} kg")
            print(f"Peso previsto: {resultado['peso_previsto']} kg")
            print(f"Diferença: {resultado['diferenca']} kg")

    def plotar_grafico(self):
        """Plota gráfico de evolução de peso."""
        self.health.carregar_dados()
        if self.health.df is None or self.health.df.empty:
            print("Nenhum dado para plotar.")
        else:
            self.health.plotar_grafico()


def main():
    """Ponto de entrada da aplicação."""
    cli = NutriAICLI()
    cli.menu_principal()


if __name__ == "__main__":
    main()
