## Dash: installation and first steps #
#
### What is Dash?
#> Dash is a Open Source Python library for creating reactive, Web-based applications. [Source](https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503)
#
#Dash allows the components of a web-based application to interact with each other, for example using a dropdown menu to select what to show on a plot. Thus, it builds up from the plotly capabilities, allowing plots to be updated even at real time. Dash produced a dashboard web application at a local url, typically [http://127.0.0.1:8050/](http://127.0.0.1:8050/).
#
### How to install it?
#[Install Dash following](https://dash.plot.ly/installation). In Windows you can do the installation within Visual Strudio. On the command line you can type the following:
#`
# python -m pip install dash==0.28.2  # The core dash backend
# python -m pip install dash-html-components==0.13.2 # HTML components
# python -m pip install dash-core-components==0.30.2 # Supercharged components
#`
#
### Initial example
#Here we are going to produce a first web entry with some markdown text and some css styling.
#
#Let's start by loading the dash libraries:

import dash
import dash_core_components as dcc  # For the interactive components
import dash_html_components as html # It will translate your text/code into html

dash_app = dash.Dash('my first dash app')

#### The layout ###
#Dash applications can contain several elements of different characteristics, from html text to graphs. The way these elements are presented is described in the application layout. Here we focus on the html components.
#
#> The layout of a Dash app describes what the app looks like. The layout is a hierarchical tree of components. The dash_html_components library provides classes for all of the HTML tags and the keyword arguments describe the HTML attributes like style, className, and id. 
#>> Ref: [dash html components](https://dash.plot.ly/dash-html-components)
#
##The dash layout can have several sections, declared as a list. The style of each section can be controlled within dash, which will translate this into [css](https://en.wikipedia.org/wiki/Cascading_Style_Sheets). The style is stated with dictionaries with a key name and its value. Let's see an example where we have a title and some subtitles. Note that now we are leaving out `children=` as it is implied.
dash_app.layout = html.Div([ #Div defines a division, section or block
    html.H1(children='Hello World'), # Title, the 'children=' is implied, so it can be omitted
    html.Div('The world is a big place', # Styled sub-title
             style=dict(color='blue')
             ),
    html.Div(['One','Two'], # Two components for this section
             style=dict(color='red',border='3px red solid')
            )
],style=dict(border='2px green solid')) # Global style


# Run the application: you will get a message of the link to put in your browser to see the result
dash_app.run_server(debug=True)

# Calling the help function:
print(help(html.Div))

