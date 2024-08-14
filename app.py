import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
         meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ])

# Define the navigation bar with the dropdown menu

header = [
            html.Img(src=os.path.join(os.getcwd(),"/assets/header.webp"),className="header-image center-image large-image"),
            html.Img(src=os.path.join(os.getcwd(),"/assets/header_m.webp"),className="header-image center-image small-image"),
         ]

nav= dbc.Nav(
                    [
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("¿Qué es la metabolómica?", header=False),
                                dbc.DropdownMenuItem("Metabolismo y Metabolitos en Plantas", href="#"),
                                dbc.DropdownMenuItem("Metabolitos", href="#"),
                                dbc.DropdownMenuItem("Metabolismo primario", href="#"),
                                dbc.DropdownMenuItem("Metabolismo secundario", href="#"),
                                dbc.DropdownMenuItem("Metabolómica en la investigación de la coca", href="#"),
                            ],
                            nav=True,
                            in_navbar=True,
                            label="INTRODUCCIÓN",
                        ),
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("PASO 1: Extracción de los compuestos presentes en las hojas", header=False,
                                                     style={'fontSize': '1rem'}, href=f"#experimento_paso_1",external_link=True),
                                dbc.DropdownMenuItem("Principios básicos de extracción química", href=f"#pbe",external_link=True),
                                dbc.DropdownMenuItem("Extracción líquido-líquido simple", href=f"#extraccion_liquido",external_link=True),
                                dbc.DropdownMenuItem("Características del disolvente de extracción", href=f"#car_sol",external_link=True),
                                dbc.DropdownMenuItem("PASO 2: Análisis de compuestos: Cromatografía de Gases", href=f"#experimento_paso_2",external_link=True),
                                dbc.DropdownMenuItem("¿Qué es una cromatografía?", href="#que_es_cro",external_link=True),
                            ],
                            nav=True,
                            in_navbar=True,
                            label="EXPERIMENTO",
                            
                            
                        ),
                        dbc.NavItem(dbc.NavLink("RESULTADOS", href="#")),
                        dbc.NavItem(dbc.NavLink("METODOLOGÍA", href="#")),
                        dbc.NavItem(dbc.NavLink("CONCLUSIONES", href="#")),
                        dbc.NavItem(dbc.NavLink("GLOSARIO", href="#")),
                        dbc.NavItem(dbc.NavLink("BIBLIOGRAFÍA", href="#")),
                    ],
                    style={'fontFamily': 'clutadella_light','backgroundColor': '#9abf99'},
                    justified=True,
                    pills=True,
                    class_name='custom-nav'
            )

portada =  dbc.Row(
        [
            html.Img(src="/assets/h_exp_1.webp",style={"width": "100%",'marginTop':'3%','marginBottom':'3   %'},className="center-image"),
        ]
                )

experimento = dbc.Container(
    dbc.Row([
                html.Div("EXPERIMENTO", className="body-title-green"), 
                html.Div(["Este estudio busca identificar los ", html.Span("compuestos químicos", id="compuestos_quimicos",className="underlined-text"),  " presentes en las cuatro variedades de coca cultivadas en el jardín del Proyecto Khoka. Para ello, se prepararon extractos con las hojas de cada variedad en diferentes ", html.Span("solventes", id="solvente_1",className="underlined-text") ," y se caracterizaron los metabolitos presentes en sus hojas mediante técnicas cromatográficas. Esto nos permitió realizar un análisis comparativo e identificar las similitudes y diferencias en la producción de estos compuestos entre las distintas variedades."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("PASO 1: ",className="body-title-1",id="experimento_paso_1"),
                html.Div("Extracción de los compuestos presentes en las hojas",className="body-title-2"),
                html.Div(["El proceso de extracción consiste en mezclar hojas secas de cada variedad de coca con diversos ", html.Span("solventes", id="solvente_2", className="underlined-text"),", utilizando calor, para extraer y concentrar los componentes presentes en las hojas y así poder analizar una muestra mediante cromatografía de gases."],
                       style={'marginTop':'1rem','marginBottom':'0rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Img(src="/assets/h_exp_2_esc.webp",style={"width": "100%",'marginTop':'4rem','marginBottom':'1rem'},className="center-image large-image"),
                html.Img(src="/assets/exp_2_m.webp",style={"width": "100%",'marginTop':'4rem','marginBottom':'1rem'},className="center-image small-image"),

                html.Div("Principios básicos de extracción química",className="body-title-3", id = "pbe",
                         style={'marginTop':'2rem','marginBottom':'3rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div(["La extracción con solventes es una técnica de separación que aprovecha las diferencias de solubilidad de los componentes de una ", html.Span("mezcla", id="mezcla_1", className="underlined-text"), ", ya sea sólida o líquida, para aislar un compuesto específico mediante la transferencia selectiva de este desde la ", html.Span("mezcla", id="mezcla_2", className="underlined-text")," original hacia una fase líquida, a través de un ", html.Span("solvente", id="solvente_3", className="underlined-text"), " orgánico como el etanol o la acetona."],
                       style={'paddingRight':'0rem','paddingLeft':'0rem'}),


                html.Div("Extracción líquido-líquido simple",className="body-title-3", id = "extraccion_liquido",
                         style={'marginTop':'2rem','marginBottom':'3rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div(["La extracción líquido-líquido es un método eficaz para separar los componentes de una ", html.Span("mezcla",id="mezcla_3", className="underlined-text")," líquida. La efectividad de esta técnica se basa en la diferencia de ",html.Span("solubilidad", id="solubilidad_1",className="underlined-text")," del compuesto que se quiere extraer en dos ",html.Span("solventes", id="solvente_4", className="underlined-text")," distintos ",html.Span("inmiscibles", id="inmiscible_1",className="underlined-text"),", es decir, que al agitar la ", html.Span("mezcla", id="mezcla_4", className="underlined-text")," el compuesto se distribuye selectivamente entre ambos solventes generando dos ",html.Span("fases",id="fases", className="underlined-text"),". Ejemplo: agua y éter de petróleo."],
                       style={'paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Img(src="/assets/h_exp_3_esc.webp",style={"width": "100%",'marginTop':'4rem','marginBottom':'1rem'},className="center-image large-image"),
                html.Img(src="/assets/exp_3_m.webp",style={"width": "100%",'marginTop':'4rem','marginBottom':'1rem'},className="center-image small-image"),

                html.Div("Características del solvente de extracción",className="body-title-3", id = "car_sol",
                         style={'marginTop':'2rem','marginBottom':'3rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div(["La extracción selectiva de un componente de una ",html.Span("mezcla", id="mezcla_5", className="underlined-text")," se logra añadiendo otro solvente que cumpla con las siguientes condiciones:"],
                       style={'paddingRight':'0rem','paddingLeft':'0rem','marginBottom':'3rem'}),

                html.Div([html.Span("Inmiscibilidad: ", className="italic-text"), "al añadir el solvente no se puede formar una ", html.Span("mezcla", id="mezcla_6", className="underlined-text")," homogénea, como al mezclar agua y aceite; aclarando que el aceite no es un buen medio de extracción."],
                       style={'paddingRight':'0rem','paddingLeft':'0rem','marginBottom':'3rem'}),      

                html.Div([html.Span("Mayor ", className="italic-text"), html.Span("solubilidad", id="solubilidad_2",className="underlined-text italic-text"),
                          html.Span(":", className="italic-text"), " el componente que se \
                          desea aislar debe ser mucho más ", html.Span("soluble", id="solubilidad_4", className="underlined-text"), 
                          " en el solvente de extracción que en el ", html.Span("solvente", id="solvente_5", className="underlined-text"), " original."],
                       style={'paddingRight':'0rem','paddingLeft':'0rem','marginBottom':'3rem'}),  

                html.Div([
                    html.Span(["Menor ", html.Span("solubilidad", id="solubilidad_3", className="underlined-text"), " de otros componentes: "], 
                              className="italic-text "),
                    "los demás componentes de la mezcla no deben ser ",
                    html.Span("solubles", id="solvente_6", className="underlined-text"),
                    " en el ",
                    html.Span("solvente", id="solvente_13", className="underlined-text"),
                    " de extracción."
                ],style={'paddingRight':'0rem','paddingLeft':'0rem','marginBottom':'3rem'}),  

                html.Div([
                    html.Span("Volatilidad", className="italic-text")," el ", html.Span("solvente", id="solvente_7", className="underlined-text"),
                    " debe ser muy volátil para que se pueda eliminar fácilmente mediante destilación o evaporación."
                ],style={'paddingRight':'0rem','paddingLeft':'0rem','marginBottom':'3rem'}), 

                html.Div([
                html.Span("Seguridad", className="italic-text")," el ",html.Span("solvente", id="solvente_8", className="underlined-text"), 
                " no debe ser tóxico ni inflamable, aunque es difícil encontrar solventes que cumplan ambos criterios. Existen solventes relativamente no tóxicos pero inflamables, como el hexano; otros no son inflamables, pero sí tóxicos, como el diclorometano o el cloroformo; y algunos son tanto tóxicos como inflamables, como el benceno."
                ],style={'paddingRight':'0rem','paddingLeft':'0rem','marginBottom':'3rem'}), 

                html.Div([
                html.Span("Solventes", className="italic-text"), html.Span(" inmiscibles con el agua:", className="italic-text"), 
                html.Span(" solventes utilizados con mayor frecuencia", className="italic-text"), html.Br(),
                "La ", html.Span("miscibilidad",id="miscible", className="underlined-text")," de un ",html.Span("solvente", id="solvente_9", className="underlined-text"),
                " orgánico con el agua depende de su polaridad:"
                ],style={'paddingRight':'0rem','paddingLeft':'0rem','marginBottom':'3rem'}), 

                html.Div([
                html.Span("Alta polaridad:", className="italic-text"),
                " los ", html.Span("solventes", id="solvente_10", className="underlined-text"),
                " orgánicos de baja polaridad son preferidos para la extracción debido a su inmiscibilidad con el agua. Entre los más utilizados se encuentran:",
                 html.Ul([
                    html.Li("Diclorometano"),
                    html.Li("Éter dietílico"),
                    html.Li("Acetato de etilo"),
                    html.Li("Hexano")
                ],style={"marginBottom": "1rem","marginTop": "1rem"}),
                "Estos ",html.Span("solventes", id="solvente_11", className="underlined-text"), 
                " orgánicos son seleccionados específicamente por su capacidad de separar eficientemente los componentes en técnicas de extracción líquido-líquido."
                ],style={'paddingRight':'0rem','paddingLeft':'0rem','marginBottom':'3rem'}), 
                
                html.Div(["PASO 2: "],className="body-title-1",id="experimento_paso_2"),
                html.Div("Análisis de compuestos: Cromatografía de Gases",className="body-title-2"),
                html.Div(["En esta etapa realizamos análisis cromatográficos de los extractos de las hojas de cada variedad de coca preparados en distintos ", 
                         html.Span("solventes", id="solvente_12", className="underlined-text")," como etanol, diclorometano y hexano."],
                         style={'marginTop':'1rem','marginBottom':'3rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("¿Qué es una Cromatografía?",className="body-title-3", id = "que_es_cro"),
                html.Div(["Es un conjunto de técnicas de laboratorio utilizadas para separar los \
                          compuestos de una ",html.Span("mezcla", id="mezcla_7", className="underlined-text"), ". Dado que los extractos de plantas contienen \
                          cientos de metabolitos, la cromatografía de gases se destaca como \
                          una técnica rápida y precisa para la identificación de cada metabolito \
                          presente. Este procedimiento implica tomar una muestra de cada \
                          extracto, calentarlo a altas temperaturas para volatilizar los compuestos, \
                          e inyectarlos en una columna hueca metálica de 20 metros, recubierta \
                          internamente con sílice u otro material finamente pulverizado. Los \
                          componentes se mueven a través de la columna a diferentes velocidades, \
                          dependiendo de su naturaleza química y empujados por un gas inerte, \
                          como nitrógeno o helio. Al final de la columna, un detector identifica los \
                          compuestos que emergen. Este resultado se registra en un ",html.Span("cromatograma.",style={'fontStyle':'italic'})],
                       style={'marginTop':'1rem','marginBottom':'0rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Img(src="/assets/h_exp_4_esc.webp",style={"width": "100%",'marginTop':'4rem','marginBottom':'1rem'},className="center-image large-image"),
                html.Img(src="/assets/exp_4_m.webp",style={"width": "100%",'marginTop':'4rem','marginBottom':'1rem'},className="center-image small-image"),
            ],
            className="container-text"
        ))

# Definir los tooltips
tooltips = []
# compuesto químico
tooltips.append(
    dbc.Tooltip("Un compuesto químico es una sustancia formada por la unión de dos o más elementos \
                diferentes de la tabla periódica. Cada compuesto se caracteriza por una fórmula química \
                específica que indica la composición exacta de sus elementos. Por ejemplo, el agua (H2O) \
                está compuesta por dos átomos de hidrógeno y uno de oxígeno.", target="compuestos_quimicos", 
                className="custom-tooltip"))

# Solvente
for i in range(1,14):
    tooltips.append(dbc.Tooltip("Un solvente es una sustancia, generalmente líquida, \
            que puede disolver otras sustancias sin \
            alterarlas químicamente para formar una solución.", target="solvente_{0}".format(str(i)), className="custom-tooltip"))
    
# Mezcla
for i in range(1,8):
    tooltips.append(dbc.Tooltip("Una mezcla es una combinación física de dos o más sustancias en la \
                    que cada componente conserva sus propiedades químicas individuales. Las sustancias \
                    en una mezcla no se combinan químicamente y, por lo tanto, pueden ser separadas por \
                    medios físicos como la filtración, la centrifugación, la decantación, o la destilación.", 
                    target="mezcla_{0}".format(str(i)), className="custom-tooltip"))

# Inmiscible
tooltips.append(dbc.Tooltip("Se refiere a una sustancia que no se mezcla y que queda separada en fases o formando una suspensión.", 
                    target="inmiscible_1".format(str(i)), className="custom-tooltip"))

# Solubilidad

for i in range(1,5):
    tooltips.append(dbc.Tooltip("Solubilidad es la capacidad de una sustancia, conocida como soluto, para disolverse en otra sustancia llamada disolvente, formando una solución homogénea. La solubilidad de un soluto en un disolvente específico depende de factores como la temperatura, el pH y la presión ambiental. Esta propiedad es fundamental para numerosos procesos en química, biología, farmacología y la vida cotidiana.", 
                        target="solubilidad_{0}".format(str(i)), className="custom-tooltip"))

# fases
tooltips.append(dbc.Tooltip("Una fase es un estado físico distinto dentro de un sistema, caracterizado \
                       por propiedades físicas y químicas uniformes. Comúnmente, se refiere a \
                       las formas distintas en las que la materia se presenta, como sólido, \
                       líquido, gas, o plasma. En un sistema heterogéneo, diferentes fases están \
                       separadas por fronteras claramente definidas, como se puede observar en una mezcla de agua y aceite.",
                       target="fases", className="custom-tooltip"))

# miscible
tooltips.append(dbc.Tooltip("Miscible se refiere a la capacidad de dos o más sustancias de mezclarse \
                            completamente entre sí para formar una solución homogénea. Esto significa que, \
                            al combinarse, se integran de manera uniforme en una sola fase, sin separarse, \
                            en ciertos rangos de temperatura, presión y composición. Un ejemplo común es el \
                            alcohol y el agua, que al mezclarse forman una solución uniforme.",
                       target="miscible", className="custom-tooltip"))

# Define the layout
app.layout= html.Div([
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
            dbc.Col(
                portada,
                xs={"size": 12, "order": 2},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 2},  # Change order to 2 on small devices
                md={"size": 12, "order": 3},
                lg={"size": 12, "order": 3},
                xl={"size": 12, "order": 3},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
                
            ),
            dbc.Col(
                experimento,
                xs={"size": 12, "order": 4},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 4},  # Change order to 2 on small devices
                md={"size": 12, "order": 4},
                lg={"size": 12, "order": 4},
                xl={"size": 12, "order": 4},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
            *tooltips
        ])
   ])
if __name__ == "__main__":
    app.run_server(debug=True)

