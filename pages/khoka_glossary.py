import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os
import csv


dash.register_page(__name__,path='/khoka_glossary')

# Define the navigation bar with the dropdown menu

header = [
            html.Img(src=os.path.join(os.getcwd(),"/assets/header.webp"),className="header-image center-image large-image"),
            html.Img(src=os.path.join(os.getcwd(),"/assets/header_m.webp"),className="header-image center-image small-image"),
         ]

portada =  dbc.Row(
        [
            html.Img(src="/assets/h_glosa_1.webp",style={"width": "100%",'marginTop':'3%','marginBottom':'3   %'},className="center-image"),
        ]
                )

glosario = dbc.Container(
    dbc.Row([
                html.Div("GLOSARIO", className="body-title-green"), 

                html.Div("Ácido",className="body-title-2"),
                html.Div(["Un ácido es una sustancia que, al disolverse en agua, produce una solución con un pH menor a 7."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("Ácido graso poliinsaturado",className="body-title-2"),
                html.Div(["Los ácidos grasos poliinsaturados son un tipo de grasa saludable presente en la dieta. Se encuentran tanto en alimentos de origen vegetal como animal, como el salmón, los aceites vegetales, y algunas nueces y semillas. Son beneficiosos para la salud, al igual que los ácidos grasos monoinsaturados. Estas grasas ayudan a reducir el colesterol malo en la sangre y pueden disminuir el riesgo de enfermedades cardíacas."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("ADN",className="body-title-2"),
                html.Div(["El ácido desoxirribonucleico, conocido también por las siglas ADN, es una molécula que contiene las instrucciones genéticas usadas para el desarrollo y funcionamiento de todos los organismos vivos y algunos virus. Es fundamental para la herencia genética."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("Agente desecante",className="body-title-2"),
                html.Div(["Un agente desecante es un material que absorbe agua del ambiente, usado para mantener productos y ambientes secos."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("Alcaloide",className="body-title-2"),
                html.Div(["Los alcaloides son compuestos naturales que las plantas producen mediante el metabolismo secundario. Estos contienen nitrógeno en su estructura molecular y son conocidos por sus potentes efectos sobre el cuerpo, incluso en dosis pequeñas. Se utilizan en medicina para aliviar el dolor y tratar enfermedades mentales. Ejemplos destacados de alcaloides incluyen la cafeína en el café y la nicotina en el tabaco, ambos estimulantes; la cocaína de la planta de coca, que además es un anestésico local; y la morfina de la amapola, empleada como analgésico."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("Aminoácidos",className="body-title-2"),
                html.Div(["Los aminoácidos son los bloques constructores de las proteínas en el cuerpo. Cada aminoácido está compuesto por un grupo amino (NH2) y un grupo carboxilo (COOH) en su estructura molecular."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("Aminoácidos esenciales",className="body-title-2"),
                html.Div(["Los aminoácidos esenciales son los aminoácidos que el cuerpo humano no puede sintetizar y, por lo tanto, deben ser obtenidos a través de la dieta. Existen nueve aminoácidos esenciales: histidina, isoleucina, leucina, lisina, metionina, fenilalanina, treonina, triptófano y valina."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("Aminoácidos no esenciales",className="body-title-2"),
                html.Div(["Los aminoácidos no esenciales son aquellos que el cuerpo humano puede sintetizar por sí mismo, por lo que no es necesario obtenerlos exclusivamente a través de la dieta. Los aminoácidos no esenciales incluyen: alanina, arginina, asparagina, ácido aspártico, cisteína, ácido glutámico, glutamina, glicina, prolina, serina y tirosina."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("Anestésico",className="body-title-2"),
                html.Div(["Un anestésico es un medicamento utilizado para inducir anestesia, lo cual provoca una pérdida reversible de sensibilidad o conciencia. Los anestésicos se clasifican en dos tipos: los generales, que causan una pérdida reversible de la conciencia, y los locales, que provocan una pérdida reversible de sensibilidad en una región específica del cuerpo sin afectar la conciencia."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("Átomo",className="body-title-2"),
                html.Div(["El átomo es la partícula más pequeña de un elemento químico que conserva todas sus propiedades químicas. Consiste en un núcleo con carga positiva, que contiene protones y neutrones, constituyendo aproximadamente el 99.9% de la masa del átomo. Los electrones, que tienen una carga negativa y son mucho más ligeros, orbitan alrededor del núcleo y determinan el tamaño del átomo."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("ATP (Adenosin trifosfato) ",className="body-title-2"),
                html.Div(["El ATP (Adenosín trifosfato) es una molécula esencial para el metabolismo energético de las células. Está compuesto por tres grupos fosfato, una base nitrogenada llamada adenina y un azúcar de tipo pentosa llamado ribosa. El ATP se produce en las mitocondrias de las células animales y en los cloroplastos de las plantas. Esta molécula actúa como una batería de energía para las células, suministrando la energía necesaria para numerosos procesos enzimáticos y reacciones químicas que facilitan la catálisis y otras funciones vitales."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),
                html.Div("Base nitrogenada ",className="body-title-2"),
                html.Div(["Las bases nitrogenadas son compuestos orgánicos con una estructura cíclica que contienen dos o más átomos de nitrógeno. Son componentes esenciales de los nucleósidos, nucleótidos, nucleótidos cíclicos, dinucleótidos y ácidos nucleicos. En el ADN, las bases nitrogenadas se representan con las letras A (adenina), T (timina), G (guanina) y C (citosina). Estas bases se emparejan de manera específica (A con T y G con C) para formar la estructura de doble hélice del ADN, permitiendo el almacenamiento y transmisión de la información genética."],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),




                html.Div("",className="body-title-2"),
                html.Div([""],
                       style={'marginTop':'3rem','marginBottom':'4rem','paddingRight':'0rem','paddingLeft':'0rem'}),



                
            ],
            className="container-text"
        ))

# Definir los tooltips
tooltips = []


# Define the layout
layout =    [ dbc.Col(
                portada,
                xs={"size": 12, "order": 2},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 2},  # Change order to 2 on small devices
                md={"size": 12, "order": 3},
                lg={"size": 12, "order": 3},
                xl={"size": 12, "order": 3},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
                
            ),
            dbc.Col(
                glosario,
                xs={"size": 12, "order": 4},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 4},  # Change order to 2 on small devices
                md={"size": 12, "order": 4},
                lg={"size": 12, "order": 4},
                xl={"size": 12, "order": 4},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
            *tooltips
        ]


