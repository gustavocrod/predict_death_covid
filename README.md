# Um Modelo Preditivo Para Classificação de Risco de Mortalidade de Pacientes com COVID-19 no Rio Grande do Sul

Durante a pandemia de COVID-19 os sistemas de saúde do mundo inteiro enfrentam problemas sem precedentes quanto a disponibilidade e alocação de recursos comorespiradores e leitos de UTI (LATIF et al., 2020).  Estudos mostram que modelos de aprendizagem de máquina (*machine learning*) conseguem classificar chances de recuperação ou risco de óbito com até 94% de acurácia (IWENDI et al., 2020) e 0.74 de pontuação ROC (*Receiver Operating Charachteristic Curve) - AUC (Area Under the Curve*) parapredição de admissão em UTI (YADAW et al., 2020) (ASSAF et al., 2020), contribuindo para amenizar alguns dos problemas relacionados a alocação de recursos.

Os modelos de predição enfrentam pelo menos dois desafios significativos. O primeiro deles diz respeito à limpeza dos dados, isto é, eliminar erros, inconsistências ou pontos fora da curva (outliers, em inglês). O segundo desafio é encontrar modelos, características e métricas de avaliação de algoritmos de aprendizagem de máquina que garantam a credibilidade dos modelos preditivos. Com uma menção honrosa ao desafio de dispor dados para que todas as análises possam ser feitas.

O objetivo desse trabalho é propor um modelo preditivo para classificação de risco de mortalidade de pacientes com COVID-19 no estado do Rio Grande do Sul. Para atingir o objetivo, o trabalho foi dividido em duas etapas. A primeira consiste na limpeza dos dados, e a segunda é propor e validar o uso de técnicas de aprendizagem de máquina para auxiliar na tomada de decisões.

## 1. Aquisição dos dados

Os dados para a análise, no presente projeto, vêm do [Painel Corona Vírus RS](https://ti.saude.rs.gov.br/covid19/), e compreende o perído de 29/02/2020 a 11/03/2021. Essa plataforma, por sua vez, usa como fontes os dois sistemas de notificações oficiais do Ministério da Saúde no monitoramento da doença: o e-SUS Notifica e o Sistema de Informação da Vigilância Epidemiológica da Gripe (Sivep-Gripe). 

O e-SUS Notifica (que antes era chamado de e-SUS VE) é a ferramenta na qual são notificados os casos de síndrome gripal (SG) que não precisam de internação hospitalar. Casos de SG atendidos em Unidades Sentinelas são notificados no SIVEP-Gripe (Síndrome Gripal). Nos casos em que a pessoa apresenta quadro mais grave da infecção (Síndrome Respiratória Aguda Grave – SRAG) e é necessária a hospitalização, a notificação é feita no SIVEP-Gripe (SRAG Hospitalizado)..

Ambos os sistemas são utilizados pelos serviços de saúde públicos e privados e pelas secretarias municipais de saúde para realização das notificações e monitoramento dos casos e seus contactantes (sintomas, exames realizados, resultados, evolução, entre outros).

## Divisão dos notebooks

Para melhor entendimento e condução do estudo, os processos foram divididos em 4 Notebooks:

 - [1: Análise exploratória](https://github.com/gustavocrod/predict_death_covid/blob/main/1analise_exploratoria.ipynb)
 - [2: Limpeza de dados](https://github.com/gustavocrod/predict_death_covid/blob/main/2limpeza_de_dados.ipynb)
 - [3: Pre-processamento dos dados](https://github.com/gustavocrod/predict_death_covid/blob/main/3pre_processamento.ipynb)
 - [4: Análise preditiva](https://github.com/gustavocrod/predict_death_covid/blob/main/4predicao.ipynb)
