"""Módulo de previsões e análise de histórico de saúde."""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from pathlib import Path


class HealthPredictor:
    """Analisa histórico e faz previsões de evolução de peso."""

    def __init__(self, data_arquivo: str = "historico.csv"):
        """
        Inicializa o preditor de saúde.
        
        Args:
            data_arquivo: Caminho do arquivo CSV com histórico
        """
        self.data_arquivo = data_arquivo
        self.df = None
        self.modelo = None

    def carregar_dados(self) -> pd.DataFrame:
        """Carrega dados do arquivo CSV."""
        if Path(self.data_arquivo).exists():
            self.df = pd.read_csv(self.data_arquivo)
            self.df["data"] = pd.to_datetime(self.df["data"])
            return self.df
        return None

    def adicionar_peso(self, data: str, peso: float):
        """
        Adiciona registro de peso ao histórico.
        
        Args:
            data: Data no formato "YYYY-MM-DD"
            peso: Peso em kg
        """
        novo_registro = {"data": pd.to_datetime(data), "peso": peso}
        
        if self.df is None:
            self.df = pd.DataFrame([novo_registro])
        else:
            self.df = pd.concat([self.df, pd.DataFrame([novo_registro])], ignore_index=True)
        
        self.df = self.df.sort_values("data").reset_index(drop=True)
        self.salvar_dados()

    def salvar_dados(self):
        """Salva dados em arquivo CSV."""
        if self.df is not None:
            self.df["data"] = self.df["data"].dt.strftime("%Y-%m-%d")
            self.df.to_csv(self.data_arquivo, index=False)

    def prever_peso_futuro(self, dias_futuros: int = 30) -> dict:
        """
        Faz previsão de peso usando regressão linear.
        
        Args:
            dias_futuros: Dias a prever
            
        Returns:
            Dicionário com previsão
        """
        if self.df is None or len(self.df) < 2:
            return {"erro": "Dados insuficientes para previsão"}

        self.df["dias"] = (self.df["data"] - self.df["data"].min()).dt.days
        
        X = self.df["dias"].values.reshape(-1, 1)
        y = self.df["peso"].values
        
        self.modelo = LinearRegression()
        self.modelo.fit(X, y)
        
        dias_max = self.df["dias"].max()
        dias_futuros_real = np.array([dias_max + dias_futuros]).reshape(-1, 1)
        peso_previsto = self.modelo.predict(dias_futuros_real)[0]
        
        return {
            "peso_atual": round(y[-1], 2),
            "peso_previsto": round(peso_previsto, 2),
            "diferenca": round(peso_previsto - y[-1], 2),
            "dias": dias_futuros,
        }

    def plotar_grafico(self, titulo: str = "Evolução de Peso", salvar_em: str = "grafico.png"):
        """
        Plota gráfico de evolução de peso com linha de tendência.
        
        Args:
            titulo: Título do gráfico
            salvar_em: Arquivo para salvar imagem
        """
        if self.df is None or len(self.df) < 1:
            return

        plt.figure(figsize=(10, 6))
        plt.plot(self.df["data"], self.df["peso"], marker="o", label="Peso")
        
        # Linha de tendência
        if len(self.df) >= 2:
            self.df["dias"] = (self.df["data"] - self.df["data"].min()).dt.days
            X = self.df["dias"].values.reshape(-1, 1)
            y = self.df["peso"].values
            modelo = LinearRegression()
            modelo.fit(X, y)
            tendencia = modelo.predict(X)
            plt.plot(self.df["data"], tendencia, "r--", label="Tendência")
        
        plt.xlabel("Data")
        plt.ylabel("Peso (kg)")
        plt.title(titulo)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(salvar_em, dpi=100)
        plt.close()
        print(f"Gráfico salvo em {salvar_em}")
