## Dash core components #
#
#Beside html text, dash applications can include graphs, sliders, etc. Their set up is declared in the dash applicatioin layout and they are defined within the [dash core_components library](https://dash.plot.ly/dash-core-components):
#
#> The dash_core_components library generates higher-level components like controls and graphs.
#
#Import dash and both the html and core components:

import dash
import dash_core_components as dcc  # For the interactive components
import dash_html_components as html # It will translate your text/code into html

# We are going to build up a dash application with some markdown text, a dropdown menu and a graph. First we define the application:

dash_app = dash.Dash('my dash app')

## Markdown text
#We create some [markdown](https://commonmark.org/help/) text to be included later on in the layout of the dash application:
md_text = '''
# A dash application with a dropdown menu
Choose a value from the dropdown menu *below*:
'''

md = dcc.Markdown(children=md_text)

### Dropdown menu
#Next we add a dropdown menu with 3 options and a default value(see the [documentation](https://dash.plot.ly/dash-core-components) for further options). Note that the options are declared as a list and each one has properties declared as dictionaries.

dropdownmenu = dcc.Dropdown(
    options=[ #List with option to appear in the dropdown menu
        dict(label='Sine',value='sin'),
        dict(label='Cosine',value='cos'),
        dict(label='Tangent',value='tan')
    ],
    value='Sine' # This is the default value to appear in the dropdown menu
)


## Plot
#We are going to add a graph showing the sin(x) with values produced using numpy. First we generate the data and names for the axis of the plot:

import numpy as np

x_values = np.arange(0.,360.,10.)  # Degrees: Numpy array from 0. to 360., in steps of 10. 
y_values = np.sin(x_values*np.pi/180.) # Sin(x in radians)

x_title = 'x (degrees)'
y_title = 'sin(x)'

#Now we use that information to populate the layout of the plot that we want to include in the dash application. The layout of a dash plot has 2 parts: the declaration of the data and the layout that sets the axis labels, the legend, etc. Below we separate the definition of these 2 parts.

#Data to be plotted
plot_data = [{'x': x_values, 'y': y_values,
         'marker':{'color':'red','size':'10','symbol':'dot'},
         'mode': 'markers+lines',
         'name': 'Sin(x)', # Name to appear in legend 
         'type': 'scatter', # bar, contour, etc
}]

plot_layout = { # Plot set up
    'xaxis':{'title': x_title },
    'yaxis':{'title': y_title },
    'showlegend': True # To show a legend
}

# Layout for the plot
plot = dcc.Graph(id='trig_plot',figure=dict(data=plot_data,layout=plot_layout))

#dash_app.css.config.serve_locally = True
#dash_app.scripts.config.serve_locally = True

dash_app.layout = html.Div([md,dropdownmenu,plot])

# Run the application: you will get a message of the link to put in your browser to see the result
dash_app.run_server(debug=True)
