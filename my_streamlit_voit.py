import streamlit as st
st.title('Hello everyone!')
st.write("Attention ça va démarrer sur les chapeaux de roues")

import pandas as pd
st.title('Données utilisées')
voitures = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

dates = voitures['year'].drop_duplicates().sort_values()

continents = st.sidebar.selectbox("Choisissez un Continent",("US", "Europe", "Japan", "Tous"))
if continents == "US":
    data = voitures[voitures['continent'] == ' US.']
elif continents == "Europe":
    data = voitures[voitures['continent'] == ' Europe.']
elif continents == "Japan":
    data = voitures[voitures['continent'] == ' Japan.']
elif continents == "Tous":
    data = voitures
st.write(data)
     
years = st.sidebar.multiselect("Choisissez une date", dates)
data = data.loc[data['year'].isin(years)]
    
st.title('Etude de la corrélation des différents paramètres :')
import seaborn as sns
import matplotlib.pyplot as plt
viz_correlation = sns.heatmap(data.corr(), annot=True, linewidths=.5, vmin = -1, vmax= 1,cmap = "RdGy_r")
plt.suptitle("Heatmap de corrélation", size = 18)
st.pyplot(viz_correlation.figure, True)
st.write(" => Tous les paramètres semblent corrélés")

viz_1 = sns.scatterplot(data = data, x='hp', y = 'mpg', hue = 'continent')
plt.suptitle("Etude de la consommation d'essence vs le nombre de chevaux d'une voiture.", size = 18)
st.pyplot(viz_1.figure, True)
st.write(" => Plus la voiture est puissante et moins elle consomme d'essence.")
st.write(" => Les voitures les plus puissantes sont vendues aux USA.")

viz_2 = sns.scatterplot(data = data, x='weightlbs', y = 'cubicinches', hue = 'continent')
plt.suptitle("Etude du poids d'une voiture vs le nombre de cm cube des moteurs.", size = 18)
st.pyplot(viz_2.figure, True)
st.write(" => Plus la voiture est lourde plus la cylindrée est puissante.")
st.write(" => Les voitures les plus lourdes et les plus grosses cylindrée sont Américaines. La grandeur Américaine.")

