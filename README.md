# 📊 Validador de Dados de Campanhas (ETL com Streamlit + Pydantic)

Este projeto implementa um **pipeline de ETL** focado em **qualidade e validação de dados** de campanhas de marketing digital, utilizando **Pydantic** para validação de regras de negócio e **Streamlit** para interface interativa.

O objetivo é garantir que arquivos CSV (ex.: planilhas de campanhas) estejam **estruturados, tipados e consistentes** antes de serem utilizados em análises, dashboards ou pipelines analíticos.

---

## 🚀 Funcionalidades

- Upload de arquivos CSV via interface web
- Validação linha a linha com mensagens de erro detalhadas
- Tipagem forte dos dados (int, float, string, data)
- Regras de negócio aplicadas automaticamente:
  - Valores mínimos e máximos
  - Campos obrigatórios e opcionais
  - Tratamento de valores nulos
- Download do CSV validado
- Feedback visual em tempo real

---

## 🔁 Pipeline de Dados (ETL)

### 📥 Extract
- Upload do arquivo CSV pelo usuário via Streamlit

### 🔄 Transform
- Conversão automática de tipos
- Validação com **Pydantic**
- Aplicação de regras de negócio (ex.: `Amount_spent >= 0`)
- Identificação de erros por linha

### 📤 Load
- Exportação dos dados validados em CSV
- Possibilidade de integração futura com bancos de dados ou data lakes

---

## 🧠 Modelo de Validação (Pydantic)

Os dados são validados utilizando um modelo fortemente tipado:

```python
class PlanilhaVendas(BaseModel):
    Organizador: int
    Ano_Mes: str
    Dia_da_Semana: str
    Tipo_Dia: str
    Objetivo: str
    Date: date
    AdSet_name: Optional[str]
    Amount_spent: float = Field(ge=0, le=1200.00)
    Link_clicks: Optional[float]
    Impressions: Optional[float]
    Conversions: Optional[float]
    Segmentação: Optional[str]
    Tipo_de_Anúncio: str
    Fase: str
