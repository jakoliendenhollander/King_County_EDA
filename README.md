# King County data case

## Impact of location and condition on housing prices in King County

What compromises does a customer need to make if he/she wants to buy a house with mid to mid-high price in King County?

Potential compromises regarding the location and the condition of houses are:
 * having a waterfront view
 * located in a good neighbourhood, where the 15 nearest houses are large and have large plots
 * being renovated
 * being in a good condition

A multiple linear regression model was used to compute what impact these compromises have on the price.

### Create conda environment kingcounty
```
conda create --name kingcounty python=3.8.5
conda install -n kingcounty pytest==6.1.1
conda install -n kingcounty ipython
conda install -n kingcounty jupyterlab
conda install -n kingcounty seaborn
conda install -n kingcounty scikit-learn
conda install -n kingcounty statsmodels
conda install -n kingcounty bokeh
```

### Column Names and descriptions for Kings County Data Set
* **id** - unique identifier for a house
* **date** - house was sold
* **price** -  is prediction target
* **bedrooms** -  number of Bedrooms/House
* **bathrooms** -  number of bathrooms/bedrooms
* **sqft_living** -  footage of the home
* **sqft_lot** -  footage of the lot
* **floors** -  floors (levels) in house
* **waterfront** - House which has a view to a waterfront
* **view** - Has been viewed
* **condition** - How good the condition is ( Overall )
* **grade** - overall grade given to the housing unit, based on King County grading system
* **sqft_above** - square footage of house apart from basement
* **sqft_basement** - square footage of the basement
* **yr_built** - Built Year
* **yr_renovated** - Year when house was renovated
* **zipcode** - zip
* **lat** - Latitude coordinate
* **long** - Longitude coordinate
* **sqft_living15** - The square footage of interior housing living space for the nearest 15 neighbors
* **sqft_lot15** - The square footage of the land lots of the nearest 15 neighbors
