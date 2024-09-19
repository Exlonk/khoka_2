import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os

app = dash.Dash(__name__, use_pages=True , external_stylesheets=[dbc.themes.BOOTSTRAP],
         meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ])

server = app.server

header = [
            html.Img(src=os.path.join(os.getcwd(),"/assets/header.webp"),className="header-image center-image large-image"),
            html.Img(src=os.path.join(os.getcwd(),"/assets/header_m.webp"),className="header-image center-image small-image"),
         ]

nav= dbc.Nav(
                    [
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("¿Qué es la metabolómica?", header=False,
                                                     href=f"#intro_metabol_1",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("Metabolismo y Metabolitos en Plantas", 
                                                     href=f"#intro_metabol_2",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("Metabolitos", 
                                                     href=f"#intro_metabol_3",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("Metabolismo primario", 
                                                     href=f"#intro_metabol_p",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("Metabolismo secundario",
                                                     href=f"#intro_metabol_s",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("Metabolómica en la investigación de la coca", 
                                                     href=f"#intro_metabol_4",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                            ],
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("INTRODUCCIÓN", href="/",style={'padding':0}),
                        ),
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("PASO 1: Extracción de los compuestos presentes en las hojas", header=False,
                                                     style={"fontFamily":"basker_120","fontSize":"1rem"}, href=f"#experimento_paso_1",external_link=True),
                                dbc.DropdownMenuItem("Principios básicos de extracción química", href=f"#pbe",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("Extracción líquido-líquido simple", href=f"#extraccion_liquido",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("Características del disolvente de extracción", href=f"#car_sol",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("PASO 2: Análisis de compuestos: Cromatografía de Gases", href=f"#experimento_paso_2",external_link=True,style={"fontFamily":"basker_120","fontSize":"1rem"}),
                                dbc.DropdownMenuItem("¿Qué es una cromatografía?", href="#que_es_cro",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                            ],
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("EXPERIMENTO", href="/khoka-experiment", style={'padding':0}),
                            
                            
                        ),
                        dbc.DropdownMenu(
                            [

                                dbc.DropdownMenuItem("CARACTERIZACIÓN QUÍMICA POR VARIEDADES",style={"fontFamily":"basker_120","fontSize":"0.8rem"}, href=f"#caracterizacion",external_link=True),
                                dbc.DropdownMenuItem("CARACTERIZACIÓN QUÍMICA POR VARIEDADES",style={"fontFamily":"basker_120","fontSize":"0.8rem"}, href=f"#compuestos_bioactivos",external_link=True),
                                dbc.DropdownMenuItem("CROMATOGRAMAS",style={"fontFamily":"basker_120","fontSize":"0.8rem"}, href=f"#cromatogramas",external_link=True)

                            ],
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("RESULTADOS", href="/khoka-results",style={'padding':0}),    
                        ),

                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("Cromatografía de gases", header=False,
                                                    href=f"#meto_croma",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("Tiempo de Retención", href=f"#meto_tiempo",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"})

                            ],
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("METODOLOGÍA", href="/khoka_methodology",style={'padding':0}),    
                        ),
#                        dbc.NavItem(dbc.NavLink("METODOLOGÍA", href="/khoka_methodology",style={'padding':0})),
                        dbc.NavItem(dbc.NavLink("CONCLUSIONES", href="#")),
                        dbc.DropdownMenu(
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("GLOSARIO", href="/khoka_glossary",style={'padding':0}),    
                        ),
#                        dbc.NavItem(dbc.NavLink("GLOSARIO", href="#")),
                        dbc.DropdownMenu(
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("BIBLIOGRAFÍA", href="/khoka_bibliography",style={'padding':0}),    
                        ),
#                        dbc.NavItem(dbc.NavLink("BIBLIOGRAFÍA", href="#")),
                    ],
                    style={'fontFamily': 'clutadella_light','backgroundColor': '#9abf99'},
                    justified=True,
                    pills=True,
                    class_name='custom-nav'
            )

app.layout = html.Div([
            dbc.Row([
            dbc.Col(
                header,
                xs={"size": 12, "order": 1},
                sm={"size": 12, "order": 1},
                md={"size": 12, "order": 1},
                lg={"size": 12, "order": 1},
                xl={"size": 12, "order": 1},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
            dbc.Col(
                nav,
                xs={"size": 12, "order": 3},
                sm={"size": 12, "order": 3},
                md={"size": 12, "order": 2},
                lg={"size": 12, "order": 2},
                xl={"size": 12, "order": 2},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
             ]),
            dash.page_container
            ])

# Define the layout of the page
for page in dash.page_registry.values():
    print('name:', page['name'])
    print('url:', page['path'])

if __name__ == "__main__":
    app.run_server(
        debug=True)
