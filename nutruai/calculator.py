"""Módulo de cálculos nutricionais básicos."""


class Calculator:
    """Calcula métricas de saúde e nutrição."""

    @staticmethod
    def calcular_imc(peso: float, altura: float) -> dict:
        """
        Calcula o Índice de Massa Corporal (IMC).
        
        Args:
            peso: Peso em kg
            altura: Altura em metros
            
        Returns:
            Dicionário com IMC e classificação
        """
        imc = peso / (altura ** 2)
        
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"
        
        return {"imc": round(imc, 2), "classificacao": classificacao}

    @staticmethod
    def calcular_gasto_calorico(peso: float, altura: float, idade: int, sexo: str, atividade: float) -> dict:
        """
        Calcula o gasto calórico diário usando Mifflin-St Jeor.
        
        Args:
            peso: Peso em kg
            altura: Altura em cm
            idade: Idade em anos
            sexo: "M" para masculino, "F" para feminino
            atividade: Fator de atividade (1.2-1.9)
            
        Returns:
            Dicionário com TMB e TDEE
        """
        if sexo.upper() == "M":
            tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
        else:
            tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161
        
        tdee = tmb * atividade
        
        return {"tmb": round(tmb, 2), "tdee": round(tdee, 2)}

    @staticmethod
    def distribuir_macronutrientes(calorias: float, dieta: str = "balanceada") -> dict:
        """
        Distribui macronutrientes baseado no tipo de dieta.
        
        Args:
            calorias: Total de calorias diárias
            dieta: Tipo de dieta (balanceada, lowcarb, highprotein)
            
        Returns:
            Dicionário com gramas de proteína, carboidrato e gordura
        """
        if dieta == "lowcarb":
            proteina_pct, carb_pct, gordura_pct = 0.30, 0.20, 0.50
        elif dieta == "highprotein":
            proteina_pct, carb_pct, gordura_pct = 0.40, 0.40, 0.20
        else:  # balanceada
            proteina_pct, carb_pct, gordura_pct = 0.30, 0.50, 0.20
        
        return {
            "proteina_g": round((calorias * proteina_pct) / 4, 1),
            "carboidrato_g": round((calorias * carb_pct) / 4, 1),
            "gordura_g": round((calorias * gordura_pct) / 9, 1),
        }
