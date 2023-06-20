import streamlit as st
import pandas as pd
import plotly.express as px

# Read dataset vehicles_us.csv
df_vehiclesus = pd.read_csv('/Users/josemelgarejo-mini/Documents/GitHub/tripletenrepo_sd/vehicles_us.csv')

# Using plotly express
st.header('Scatter Plot of Odometer vs Price')
fig = px.scatter(df_vehiclesus, x='odometer', y='price')

fig.update_xaxes(title='Odometer')
fig.update_yaxes(title='Price')
fig.update_layout(title='Scatter Plot of Odometer vs Price')

fig.update_yaxes(range=[0, 100000])

st.write(fig)

# Calculate mean price of vehicles

mean_price = df_vehiclesus['price'].mean()

st.header('Histogram of Price - Color Vehicles')
fig = px.histogram(df_color, x='price', nbins=300)

# Create dataframes of monochrome and color vehicles

df_monochrome = df_vehiclesus[df_vehiclesus['Monochrome'] == 'Monochrome']
df_color = df_vehiclesus[df_vehiclesus['Monochrome'] == 'Color']

# Calculate mean pricing for monochrome and color vehicles

color_mean = df_color['price'].mean()
monochrome_mean = df_monochrome['price'].mean()
print("The mean for color vehicles is:", color_mean)
print("The mean for monochrome vehicles is:", monochrome_mean)




# Update labels and title
fig.update_xaxes(title_text='Price')
fig.update_yaxes(title_text='Frequency')
fig.update_layout(title_text='Histogram of Price - Color Vehicles')
fig.update_xaxes(range=[0, 80000])
fig.update_yaxes(range=[0, 6000])
fig.add_shape(type="line", x0=color_mean, y0=0, x1=color_mean, y1=6000,
              line=dict(color="red", width=1, dash="dash"))
fig.add_annotation(x=color_mean, y=4000, text=f"Mean: {color_mean:.2f}", showarrow=False,
                   font=dict(color="red"))

# Display the plot
st.write(fig)





