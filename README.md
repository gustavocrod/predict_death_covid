Neste projeto de *machine learning* utilizamos uma abordagem "5-step", compredida por:

 - I. Definir o Problema
 - [II. Preparar os dados](https://github.com/gustavocrod/predict_death_covid/blob/main/2_data_preparation.ipynb)
 - [III. Testar e avaliar de modelos](https://github.com/gustavocrod/predict_death_covid/blob/main/3_spotcheck_algorithms.ipynb)
 - [IV. Melhorar os resultados](https://github.com/gustavocrod/predict_death_covid/blob/main/4_improving_results.ipynb)
 - V. Apresentar os resultados
 
 ---

# I. Definição do Problema

## Modelo preditivo para prognóstico de pacientes com COVID-19

Durante a pandemia de _coronavirus disease 2019_ (COVID-19) os sistemas de saúde do mundo inteiro enfrentam problemas quanto a disponibilidade e alocação de recursos como respiradores e leitos de UTI (Unidade de Terapia Intensiva). Políticas e decisões críticas estão sendo tomadas quanto a priorização de pacientes com a doença e, em países como o Brasil, existem regras que definem quem tem direito a leitos de UTI. Em alguns lugares, devido a urgência e falta de dados mais precisos, a política tem sido [priorizar as pessoas mais jovens para a ocupação dos leitos de UTI](https://www.nsctotal.com.br/colunistas/dagmara-spautz/estado-oficializa-criterio-que-da-prioridade-a-mais-jovens-e-saudaveis). Em estados como o Rio Grande do Sul, [não há leitos para todos os pacientes em estado grave](https://www.estado.rs.gov.br/mesmo-com-expansao-de-leitos-45-rodada-confirma-pressao-sobre-capacidade-hospitalar-e-rs-em-bandeira-preta), consequentemente, é preciso colocar em prática políticas de priorização da alocação dos leitos com base no estado clínico do paciente.

Estudos mostram que modelos de aprendizagem de máquina (_machine learning_) conseguem predizer a chance de óbito de um paciente positivo para COVID-19 com até 0,99 de pontuação AUC-ROC (Area Under the Curve - Receiver Operating Charachteristic Curve).  Por se tratar de um contexto crítico (pandemia erisco de vida), os modelos preditivos devem ser robustos, seguros e transparentes, semc omprometer a ética. Um dos principais desafios é desenvolver e garantir a credibilidade desses modelos.

Neste trabalho, propomos um modelo preditivo baseado em florestas aleatórias para classificação de risco de óbito para pacientes confirmados de COVID-19 no estado do Rio Grande do Sul/Brasil. Utilizamos a pontuação AUC-ROC para avaliar a performance do modelo. Este é um indicador importante pois nos fornece uma medida da precisão total do modelo independente de um limiar particular. O desenvolvimento do modelo é explanado utilizando o guia TRIPOD para atenuar o risco da falta de detalhes. Utilizamos também da validação cruzada 5-fold para validar internamente o modelo e, desta forma, reduzir o risco de enviesamento.
