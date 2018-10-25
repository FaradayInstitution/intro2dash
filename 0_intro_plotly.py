## Introduction to Plotly for Python
#
### What is Plotly?
#
#Plotly is both a company and an open source library for creating interactive plots. The data shown in an interactive plotly plot cannot be modified.  
#
### How to install it?
#
#Follow the official instruction [here](https://plot.ly/python/getting-started/), basically:
#`
#pip install plotly
#`
#
### Offline plots
#
#Plotly provides an on-line dashboard where you can store your plots. Nevertheless, we can create plotly plots offline and store them as an html file and open them with a browser.

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go 

# We define some data to be plotted:
deg = np.arange(0.,360.,10.)   # Degrees: Numpy array from 0. to 360., in steps of 10.
sin = np.sin(deg*np.pi/180.) # Sine(x in radians)
cos = np.cos(deg*np.pi/180.) # Cosine
tan = np.tan(deg*np.pi/180.) # Tangent

#In plotly for python, data is stored as a list: each element of the list will be defined as a 'plot' by itself. Let's see this by defining a scatter plot object for the sine we have calculated above:

trace_sin = go.Scatter( 
            x = deg,
            y = sin,
            mode = 'markers', # We will use markers (or symbols for this plot)
            name = 'Sine') # The name to appear on the legend or when we hover over the data

#For further information on the available option within plotly.graph_obj check the [documentation](https://plot.ly/python/reference/#scatter).
#Now we define the data list and plot this:

data = [trace_sin]
pyo.plot(data, filename='trig1.html', auto_open=False)

# If you are running python on the command line, make sure to have auto_open set to False, so the propmt is not hunged up. Open the file with the figure from your favourite browser.

#The plot we have produced does not have axis laberls, title, etc. All these aspects are defined in the layout. Each element in the layout is defined using python dictionaries where a key name and its value are given. All the available options fot each element are detailed in the plotly documentation, for example for the [yaxis](https://plot.ly/python/reference/#layout-yaxis).

layout = go.Layout(title='Trigonometry',
                   xaxis=dict(title='Degrees'),
                   yaxis=dict(title='Trigonometry function',range=[-1.,1.]),
                   showlegend=True
                  )
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='trig2.html', auto_open=False)

# Let's define 2 more data elements, one for the cosine and one for the tangent:
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


for trace in [trace_cos, trace_tan]:
    data.append(trace)

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='trig3.html', auto_open=False)

