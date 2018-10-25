## Plotly plot within Dash
#
#Dash can include plots made using the plotly library, which is more flexible than using Dash alone. We are going to include a plotly plot in a dash application.
#
#We start by importing plotly and the rest of the packages we need. Then we define the Dash application.

import dash
import dash_core_components as dcc  
import dash_html_components as html 
from dash.dependencies import Input, Output # This is needed in callbacks
import numpy as np
import plotly.graph_objs as go

dash_app = dash.Dash('my dash app')

## Markdown text
md_text = '''
# A dash application with a dropdown menu
Choose a value from the dropdown menu *below*:
'''

md = dcc.Markdown(children=md_text)

### Dropdown menu
dropdownmenu = dcc.Dropdown(id='dropdown',
    options=[ #List with option to appear in the dropdown menu
        dict(label='Sine',value='sin'),
        dict(label='Cosine',value='cos'),
        dict(label='Tangent',value='tan')
    ],
    value='sin' # This is the default value to appear in the dropdown menu
)

## Plot
# We generate data with numpy
deg = np.arange(0.,360.,10.)   
sin = np.sin(deg*np.pi/180.) 
cos = np.cos(deg*np.pi/180.) 
tan = np.tan(deg*np.pi/180.) 

# We define plotly scatter plots
trace_sin = go.Scatter( 
            x = deg,
            y = sin,
            mode = 'markers', 
            name = 'Sine')
trace_cos = go.Scatter( 
            x = deg,
            y = cos,
            mode = 'lines', 
            name = 'Cosine', 
)
trace_tan = go.Scatter( 
            x = deg,
            y = tan,
            mode = 'lines+markers', 
            name = 'Tangent', 
)

plot_data = [trace_sin, trace_cos, trace_tan]

# We define the plot layout using the plotly function `go.Layout`.
plot_layout = go.Layout(
    title='Trigonometry',
    xaxis=dict(title='x (degrees)'),
    yaxis=dict(title='Trigonometric function',range=[-1.,1.]),
    showlegend=True
)

# Layout for the plot
plot = dcc.Graph(id='trig_plot')

# We combine the 3 elements into the dash application
dash_app.layout = html.Div([md,dropdownmenu,plot])

## Callback
#Once the Dash application is defined, then the connections can be made. The connections are done through a callback function decorator ,`@app.callback`,  plus a function that will establish what happens in the update.
#
#In this case we use a 'callback' to connect the dropdown menu (Input) to what is being plot in the figure (Output). Below, the `component_id=` and the `component_property=` can actually be omitted as they are implicitley assumed. Note also, that the input is declared as a list, as it can contain several elements.
@dash_app.callback(
    Output(component_id='trig_plot',component_property='figure'),
    [Input(component_id='dropdown', component_property='value')])

def update_plot(input_value):
    plot_data = [eval('trace_'+str(input_value))]
    figure2update = dict(data=plot_data,layout=plot_layout)
    return figure2update

# Run the application: you will get a message of the link to put in your browser to see the result
dash_app.run_server(debug=True)
