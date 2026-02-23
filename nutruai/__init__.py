"""NutriAI - Sistema inteligente de monitoramento nutricional."""

__version__ = "0.1.0"
__author__ = "allysonarm-lang"

from .calculator import Calculator
from .health import HealthPredictor

__all__ = ["Calculator", "HealthPredictor"]
