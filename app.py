import streamlit as st
import pandas as pd
import plotly.express as px

# Import data file "vehicles_us.csv"

rawurl = 'https://raw.githubusercontent.com/jmmelgarejo/tripletenrepo_sd/main/vehicles_us.csv'
df_vehiclesus = pd.read_csv(rawurl)

# Create columns for monochrome and color using paint_color column

df_vehiclesus['Monochrome'] = 'Color'
df_vehiclesus.loc[df_vehiclesus['paint_color'].isin(['black', 'white']), 'Monochrome'] = 'Monochrome'

# Eliminate NaN values for 4wd assuming 1=4x4 or "Yes" and 0=2wd or "No"

df_vehiclesus['is_4wd'].fillna('0', inplace=True)

for index, row in df_vehiclesus.iterrows():
    if row['is_4wd'] == 1.0:
        df_vehiclesus.loc[index, '4x4'] = 'Yes'
    else:
        df_vehiclesus.loc[index, '4x4'] = 'No'

# Create mileage categories to sort via mileage to 100k

for index, row in df_vehiclesus.iterrows():
    if row['odometer'] < 25000:
        df_vehiclesus.loc[index, 'Mileage'] = '<20k'
    elif row['odometer'] >= 25000 and row['odometer'] < 50000:
        df_vehiclesus.loc[index, 'Mileage'] = '25k - 50k'
    elif row['odometer'] >= 50000 and row['odometer'] < 75000:
        df_vehiclesus.loc[index, 'Mileage'] = '50k - 75k'
    elif row['odometer'] >= 75000 and row['odometer'] < 100000:
        df_vehiclesus.loc[index, 'Mileage'] = '75k - 100k'
    else:
        df_vehiclesus.loc[index, 'Mileage'] = '>100k'

# Calculate mean price of vehicles

mean_price = df_vehiclesus['price'].mean()

# Create dataframes of monochrome and color vehicles

df_monochrome = df_vehiclesus[df_vehiclesus['Monochrome'] == 'Monochrome']
df_color = df_vehiclesus[df_vehiclesus['Monochrome'] == 'Color']

# Calculate mean pricing for monochrome and color vehicles

color_mean = df_color['price'].mean()
monochrome_mean = df_monochrome['price'].mean()     

# Calculate the mean for color and monochrome by drivetrain

color_4x4_mean = (df_color[df_color['4x4'] == 'Yes']['price']).mean()
color_2wd_mean = (df_color[df_color['4x4'] == 'No']['price']).mean()
monochrome_4x4_mean = (df_monochrome[df_monochrome['4x4'] == 'Yes']['price']).mean()
monochrome_2wd_mean = (df_monochrome[df_monochrome['4x4'] == 'No']['price']).mean()

# Create Scatter Plot to Show Odometer vs. Price
st.header("Odometer vs. Price")
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
