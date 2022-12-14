# Library

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

'''
Import and Export of goods and services decrease 
the currency risk and better profit for the country. 
If the import and export increases then the country's 
economy condition is also going better as the year passed.  
'''

# Load Dataset
df = pd.read_csv("Import_Export_of_goods_world_development_data.csv")
df

# Remove None Value
df = df.dropna(axis=0) 
df

# Rename Column of Dataset
df.rename(columns={'Country Name': 'country'}, inplace=True)
df.head(1)

# Divide dataset for Population growth & Energy Consumption
imp  = df.loc[df['Series Code'] == "BM.GSR.GNFS.CD"]
exp  = df.loc[df['Series Code'] == "BX.GSR.GNFS.CD"]

# Remove unnecessary column
imp.drop(['Country Code','Series Name', 'Series Code'], axis=1, inplace=True)
exp.drop(['Country Code','Series Name', 'Series Code'], axis=1, inplace=True)

imp.set_index('country', inplace=True)
exp.set_index('country', inplace=True)

# Graph Plot Functions
    # - These function get different parameters
    # - Dataframe 
    # - Countries Name 
    # - Years 
    # - Title of graph
    # - filename that saved in local file

def graph_plot(df, countries, years, title, filename):
    # figure size is the graph image size
    # This is a simple graph.
    df.loc[countries, years].T.plot(figsize=(14, 8)) 
    title = plt.title(title) 
    plt.savefig(filename)
    plt.show()

def graph_plot2(df, countries, years, title,  filename):
    # figure size is the graph image size
    # This graph type is Area.
    df.loc[countries, years].T.plot(kind='area', figsize=(14, 8))
    title = plt.title(title)
    plt.savefig(filename)
    plt.show()

def graph_bar(df, country, years, title, filename):
    # figure size is the graph image size
    # This is Bar graph
    df.loc[country, years].plot(kind='bar',figsize=(14, 8))
    title = plt.title(title)
    plt.savefig(filename)
    plt.show()

def graph_barh(df, countries, years, title, filename):
    # figure size is the graph image size
    # This is Barh graph
    df.loc[countries, years].transpose().plot(kind='barh', figsize=(20, 14), stacked=False)
    title = plt.title(title)
    plt.savefig(filename)
    plt.show()

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw=None, cbarlabel="", **kwargs):
# Create a heatmap from a numpy array and two lists of labels.
#     - data - A 2D numpy array of shape (M, N).
#     - row_labels - A list or array of length M with the labels for the rows.
#     - col_labels - A list or array of length N with the labels for the columns.

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def graph_heatmap(df, countries, years, title, filename):
    fig, ax = plt.subplots(figsize=(7, 7))
    
    im, cbar = heatmap(df[years].T, df[years], countries, ax=ax,
                       cmap="plasma", cbarlabel=title)
    plt.savefig(filename)
    fig.tight_layout()
    plt.show()



# Years & Country Information
    # - Year used 1980-2021
    # - Countries used 'United Kingdom', 'South Africa', 'France', 'Germany'

imp

years = ['1980 [YR1980]', '1985 [YR1985]', '1990 [YR1990]', '1995 [YR1995]', '2000 [YR2000]', 
         '2005 [YR2005]', '2010 [YR2010]', '2015 [YR2015]', '2020 [YR2020]',]

countries = ['United Kingdom', 'South Africa', 'France', 'Germany']



# Imports of goods and services Line Graph 
graph_plot(imp, countries, years, "Imports of goods and services (BoP, current US$)", "imp_1.jpg")

# Imports of goods and services Bar Graph
graph_bar(imp, countries, years, 'Imports of goods and services (BoP, current US$)', "imp_2.jpg")

# Imports of goods and services HeatMap
graph_heatmap(imp, countries, years, "Imports of goods and services (BoP, current US$)", "imp_3.jpg")

# Exports of goods and services Line Graph
graph_plot(exp, countries, years, 'Exports of goods and services (BoP, current US$)', "exp_1.jpg")

# Exports of goods and services Bar Graph
graph_bar(exp, countries, years, 'Exports of goods and services (BoP, current US$)', "exp_2.jpg")

# Exports of goods and services Heat Graph
graph_heatmap(exp, countries, years, "Exports of goods and services (BoP, current US$)", "exp_3.jpg")



imp[years].T

exp[years].T