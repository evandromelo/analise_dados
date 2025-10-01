# DESCRIÇÃO DOS DATASETS

Todos os dados são simulados com base em padrões reais de experimentos agrícolas.

## 1. umidade_solo.csv
- **Descrição**: Dados de sensores de umidade em diferentes profundidades.
- **Variáveis**:
  - `data`: data da medição
  - `profundidade_cm`: profundidade do sensor (10, 20, 30, 40 cm)
  - `umidade_pct`: umidade volumétrica do solo (%)

## 2. irrigacao_gotejamento.csv
- **Descrição**: Ensaios de uniformidade em sistemas de irrigação por gotejamento.
- **Variáveis**:
  - `pressão_bar`: pressão no início da linha
  - `vazao_lh`: vazão média por emissor
  - `uniformidade_%`: coeficiente de uniformidade Christiansen

## 3. clima_horario.csv
- **Descrição**: Dados horários de uma estação meteorológica.
- **Variáveis**:
  - `radiacao_wm2`: radiação solar global
  - `temperatura_c`: temperatura do ar
  - `umidade_rel_%`: umidade relativa
  - `vento_ms`: velocidade do vento

## 4. consumo_tratores.csv
- **Descrição**: Consumo de combustível em operações agrícolas.
- **Variáveis**:
  - `modelo`: modelo do trator
  - `carga`: nível de carga (leve, média, pesada)
  - `consumo_lh`: consumo horário de diesel (L/h)

## 5. producao_cultivos.csv
- **Descrição**: Produtividade de cultivos por sistema de plantio.
- **Variáveis**:
  - `cultura`: tipo de cultura
  - `sistema_plantio`: método de preparo do solo
  - `produtividade_t_ha`: rendimento em toneladas por hectare

---

