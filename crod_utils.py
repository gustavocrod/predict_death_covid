import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap, BoundaryNorm
from sklearn import neighbors
import matplotlib.patches as mpatches
import graphviz
import seaborn as sns
from sklearn.tree import export_graphviz
import matplotlib.patches as mpatches
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def plot_decision_tree(clf, feature_names, class_names):
    """

    :param clf: instancia do classificador
    :param feature_names: df.columns
    :param class_names: target.unique()
    :return:
    """
    # This function requires the pydotplus module and assumes it's been installed.

    export_graphviz(clf, out_file="crod_tree_temp.dot", feature_names=feature_names, class_names=class_names, filled = True, impurity = False)
    with open("crod_tree_temp.dot") as f:
        dot_graph = f.read()
    # Alternate method using pydotplus, if installed.
    # graph = pydotplus.graphviz.graph_from_dot_data(dot_graph)
    # return graph.create_png()
    return graphviz.Source(dot_graph)




def plot_horizontal_bar(df, column, xlabel, title, fix_distance=100, hide_ylabel=True, fontsize=14):
    """
    plota um coutplot horizontal com valores anotados

    :param df: dataframe
    :param column: nome da coluna para plotar a contagem
    :param xlabel: xlabel
    :param title: titulo
    :param fix_distance: valor para somar ou diminuir da distancia da barra
    :param hide_y_label: desabilitar ylabels
    :return:
    """
    df1 = pd.DataFrame(df[column].value_counts(), columns=[column])
    ax = sns.barplot(x=column, y=df1.index, data=df1, palette='mako')

    ax.set_title(title, fontsize=fontsize + 4, pad=30)

    if hide_ylabel:
        ax.set_ylabel('')

    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.secondary_xaxis('top')
    # ax.annotate('*Dados de 2013 à 2020\n**Valores do estado do RS', xy=(830, 70), xycoords='figure pixels')

    # adicionar valor à barra
    for i, value in enumerate(df1[column]):
        ax.text(value + fix_distance, i + 0.05, "{0:.0f}".format(value), color='white', fontweight='bold', fontsize=fontsize - 2)

    # tamanho dos e yticks labels
    ax.tick_params(axis='both', which='major', labelsize=fontsize - 2)
    
def plot_feature_importances(df, column, top=False):
    """

    :param df: df
    :param column: df['column']
    :return:
    """
    fontsize = 12

    rf = RandomForestClassifier()
    rf.fit(df.drop(column, axis=1), df[column])
    
    plt.style.use('seaborn-whitegrid')
    importance = rf.feature_importances_
    importance = pd.DataFrame(importance, index=df.drop(column, axis=1).columns, columns=["Importância"])
    importance = importance.sort_values(by='Importância', ascending=True)
    if top:
        importance = importance.tail()
    
    fig_dims = (12, 8)
    fig, ax = plt.subplots(figsize=fig_dims)
    
    sns.barplot(x="Importância", y=importance.index, data=importance, palette='mako', ax=ax)
    ax.set_title("Importância das características\nGini Floresta Aleatória", fontsize=fontsize + 4, pad=30)
    
    ax.set_xlabel("Importância", fontsize=fontsize)
    ax.secondary_xaxis('top')
   
    # adicionar valor à barra
    for i, value in enumerate(importance['Importância']):
        ax.text(value, i + 0.05, "{0:.0f}".format(value), color='white', fontweight='bold', fontsize=fontsize - 2)

    # tamanho dos e yticks labels
    ax.tick_params(axis='both', which='major', labelsize=fontsize - 2)
    plt.tight_layout()
    fig.savefig("imgs/feature_importance.png")


def show_values_on_bars(axs, fix_distance, fontsize):
    def _show_on_single_plot(ax):
        for p in ax.patches:
            _x = p.get_x() + p.get_width() / 2  # divide por 2 pra ficar no meio
            _y = p.get_y() + p.get_height() + fix_distance  # mais valor pra n ficar colado na altura da barra
            value = '{:.0f}'.format(p.get_height())
            ax.text(_x, _y, value, ha="center", fontsize=fontsize - 2, color='black',)

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)


def plot_vertical_bar(df, column, ylabel, title, fix_distance, hue=None, hide_xlabel=True, fontsize=14, ticklabels=None):
    """
     plota um coutplot vertical com valores anotados
    :param df: dataframe
    :param column: coluna para contagem
    :param ylabel: ylabel
    :param title:
    :param fix_distance: valor para somar ou diminuir da distancia da barra
    :param hue: coluna para plotar hue
    :param hide_xlabel:
    :return:
    """
    if hue:
        ax = sns.countplot(x=column, data=df, hue=hue, palette='mako')
    else:
        ax = sns.countplot(x=column, data=df, palette='mako')

    show_values_on_bars(ax, fix_distance, fontsize)

    ax.set_title(title, fontsize=fontsize + 4, pad=30)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    if hide_xlabel:
        ax.set_xlabel('')
    ax.secondary_yaxis('right')
    #ax.annotate('*Valores do estado do RS', xy=(100, 650), xycoords='figure pixels')

    ax.tick_params(axis='both', which='major', labelsize=fontsize - 2)

    if ticklabels:
        ax.set_xticklabels(ticklabels)


def print_df_dimensions(df):
    print("DIMENSÕES DO DATAFRAME:")
    print(f"Linhas:\t\t{df.shape[0]}")
    print(f"Colunas:\t{df.shape[1]}")


def get_percents(df, column):
    """
        Retorna a quantidade e a porcentagem de valores em uma coluna
    :param df: df
    :param column: nome da coluna
    :return:
    """
    df1 = df[column].value_counts().rename_axis(column).reset_index(name='QTD')
    df2 = (df[column].value_counts(normalize=True) * 100).rename_axis(column).reset_index(name='%').drop(
        columns=column)
    return pd.concat([df1, df2], axis=1)

