import pandas as pd
import plotly.express as px
import streamlit as st

# Get Pandas version
print("Pandas version:", pd.__version__)

# Get Streamlit version
print("Streamlit version:", st.__version__)

# Import data file "vehicles_us.csv"

rawurl = 'https://raw.githubusercontent.com/jmmelgarejo/tripletenrepo_sd/main/vehicles_us.csv'
df_vehiclesus = pd.read_csv(rawurl)

# Create columns for monochrome and color using paint_color column

df_vehiclesus['Monochrome'] = 'Color'
df_vehiclesus.loc[df_vehiclesus['paint_color'].isin(['black', 'white']), 'Monochrome'] = 'Monochrome'

# Calculate mean price of vehicles

mean_price = df_vehiclesus['price'].mean()

# Create dataframes of monochrome and color vehicles

df_monochrome = df_vehiclesus[df_vehiclesus['Monochrome'] == 'Monochrome']
df_color = df_vehiclesus[df_vehiclesus['Monochrome'] == 'Color']

# Calculate mean pricing for monochrome and color vehicles

color_mean = df_color['price'].mean()
monochrome_mean = df_monochrome['price'].mean()     

# Create Scatter Plot to Show Odometer vs. Price
st.header("Price Analysis of Vehicles - Overall Findings")
fig_odo_price = px.scatter(df_vehiclesus, x='odometer', y='price')

fig_odo_price.update_xaxes(title='Odometer')
fig_odo_price.update_yaxes(title='Price')
fig_odo_price.update_layout(title='Scatter Plot of Odometer vs Price')

fig_odo_price.update_yaxes(range=[0, 100000])

# Show Odometer vs. Price Scatter Plot

st.write(fig_odo_price)

# Create Histogram Graph to Show Price for All Vehicles

show_histogram = st.checkbox('Show Histogram')

if show_histogram:
    st.header("Price - All Vehicles")
    fig_price_all = px.histogram(df_vehiclesus, x='price', nbins=300)

# Update labels and title
    fig_price_all.update_xaxes(title_text='Price')
    fig_price_all.update_yaxes(title_text='Frequency')
    fig_price_all.update_layout(title_text='Histogram of Price - All Vehicles')
    fig_price_all.update_xaxes(range=[0, 80000])
    fig_price_all.update_yaxes(range=[0, 6000])
    fig_price_all.add_shape(type='line', x0=mean_price, y0=0, x1=mean_price, y1=6000,
              line=dict(color='red', width=1, dash='dash'))
    fig_price_all.add_annotation(x=mean_price, y=4000, text=f"Mean: {mean_price:.2f}", showarrow=False,
                   font=dict(color='red'))

# Show Price Histogram
    st.write(fig_price_all)