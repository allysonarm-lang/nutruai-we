"""Testes para o módulo calculator."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from nutruai.calculator import Calculator


def test_calcular_imc():
    """Testa cálculo de IMC."""
    calc = Calculator()
    resultado = calc.calcular_imc(70, 1.75)
    assert resultado["imc"] == 22.86
    assert resultado["classificacao"] == "Peso normal"


def test_calcular_imc_sobrepeso():
    """Testa classificação sobrepeso."""
    calc = Calculator()
    resultado = calc.calcular_imc(80, 1.75)
    assert resultado["classificacao"] == "Sobrepeso"


def test_gasto_calorico():
    """Testa cálculo de gasto calórico."""
    calc = Calculator()
    resultado = calc.calcular_gasto_calorico(70, 175, 30, "M", 1.55)
    assert "tmb" in resultado
    assert "tdee" in resultado
    assert resultado["tdee"] > resultado["tmb"]


def test_macronutrientes():
    """Testa distribuição de macronutrientes."""
    calc = Calculator()
    resultado = calc.distribuir_macronutrientes(2000, "balanceada")
    
    # Verifica se os valores somam aproximadamente 2000 calorias
    calorias_totais = (resultado["proteina_g"] * 4 + 
                      resultado["carboidrato_g"] * 4 + 
                      resultado["gordura_g"] * 9)
    
    assert 1900 < calorias_totais < 2100


if __name__ == "__main__":
    test_calcular_imc()
    test_calcular_imc_sobrepeso()
    test_gasto_calorico()
    test_macronutrientes()
    print("✅ Todos os testes passaram!")
