import streamlit as st
from streamlit_card import card
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import folium
from streamlit_folium import st_folium
import time
from streamlit_echarts import st_echarts
import pytrends
from pytrends.request import TrendReq
import requests
import pandas as pd
from streamlit_extras.let_it_rain import rain 
import plotly.graph_objects as go

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Mando Setas Meli", page_icon="🍄")

current_time = time.ctime()

with st.sidebar:
    st.write('Prototipo Mando Rentabilidad')
st.title("Mandos 🎮 Setas Meli 🍄")
a = st.selectbox("Selecciona un Mando 🎮", ("Histórico y 2024", "Estrategia", "Alarmas", "Recomendaciones"), index=None, placeholder="Choose an option")

if a == "Histórico y 2024":
  colored_header(
    label="Mando 1: Modelación Histórica",
    description="Costos, Ventas, Rentabilidades",
    color_name="violet-70",
  )
  b = st.selectbox('Selecciona un año de análisis', ('2018', '2019', '2020', '2021', '2022', '2023', '2024'))
  if b:
      st.write('Desempeño financiero en el año ', a)
      col4, col5 = st.columns(2)
      with col4:
          fig1 = go.Figure(data=[go.Sankey(
            node = dict(
              pad = 15,
              thickness = 20,
              line = dict(color = "black", width = 0.5),
              label = ["Fuente1", "Fuente2", "Fuente 3", "Online", "Offline", "Ingresos Totales"],
              color = "blue"
            ),
            link = dict(
              source = [0, 1, 2, 3, 4], # indices correspond to labels, eg A1, A2, A1, B1, ...
              target = [3, 4, 3, 5, 5],
              value = [8, 4, 5, 13, 4]
          ))])
        
          fig1.update_layout(title_text="Ingresos", font_size=10)
          st.plotly_chart(fig1, theme="streamlit")
      
      with col5:
          fig1 = go.Figure(data=[go.Sankey(
            node = dict(
              pad = 15,
              thickness = 20,
              line = dict(color = "black", width = 0.5),
              label = ["Egresos Totales", "Necesidades", "Gastos", "Inversiones", "Vivienda", "Estudio", "Alimentación", "Transporte", "Entretenimiento", "Viajes", "Acciones", "Activos", "Criptomonedas", "Bonos"],
              color = "red"
            ),
            link = dict(
              source = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
              target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
              value = [44, 44, 44, 10, 20, 10, 22, 22, 10, 14, 10, 10, 10]
          ))])
        
          fig1.update_layout(title_text="Gastos", font_size=10)
          st.plotly_chart(fig1, theme="streamlit")
  
      
      col1, col2, col3 = st.columns(3)
      with col1:
        acelerometro1 = {
              "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
              "series": [
                  {
                      "name": "Pressure",
                      "type": "gauge",
                      "axisLine": {
                          "lineStyle": {
                              "width": 10,
                          },
                      },
                      "progress": {"show": "true", "width": 10},
                      "detail": {"valueAnimation": "true", "formatter": "{value}"},
                      "data": [{"value": 50, "name": "Liquidez"}],
                  }
              ],
          }
      
        st_echarts(options=acelerometro1)
      
      with col2:
        acelerometro2 = {
              "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
              "series": [
                  {
                      "name": "Pressure",
                      "type": "gauge",
                      "axisLine": {
                          "lineStyle": {
                              "width": 10,
                          },
                      },
                      "progress": {"show": "true", "width": 10},
                      "detail": {"valueAnimation": "true", "formatter": "{value}"},
                      "data": [{"value": 85, "name": "Endeudamiento"}],
                  }
              ],
          }
      
        st_echarts(options=acelerometro2)
          
      with col3:
        acelerometro3 = {
              "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
              "series": [
                  {
                      "name": "Pressure",
                      "type": "gauge",
                      "axisLine": {
                          "lineStyle": {
                              "width": 10,
                          },
                      },
                      "progress": {"show": "true", "width": 10},
                      "detail": {"valueAnimation": "true", "formatter": "{value}"},
                      "data": [{"value": 20, "name": "Solvencia"}],
                  }
              ],
          }
        st_echarts(options=acelerometro3)




if a == "Estrategia":
  colored_header(
    label="Mando 2: Estrategia de Datos e Inteligencia Artificial",
    description="Procesos, Indicadores y Monitoreo",
    color_name="violet-70",
  )
  st.markdown(
    """
    - 🗣️ _    Titularidad
    - ♻️ _    Ciclo de Vida
    - 🏗️ _     Arquitectura
    - 🧮 _     Modelación
    - ⏲️ _     Operación
    - 🛂 _     Seguridad
    - 🚫 _     Privacidad
    - 🤝 _     Conciliación
    - 💡 _     Referentes
    - 🌊 _     Lago
    - ⚠️ _     Elementos Críticos
    - ℹ️ _     Metadata
    - ✅ _     Calidad
    - 🔄 _     Integración
    - ✝️ _     Políticas
    - ▶️ _     Estándares
    - 🔁 _     Procesos
    """
  )



if a == "Alarmas":
  colored_header(
    label="Mando 3: Alarmas Operativas, Financieras y Comerciales",
    description="Procesos, Indicadores y Monitoreo",
    color_name="violet-70",
  )
  st.write("In real time monitoring at: ", current_time)
  st.subheader('Costos Operativos del día de hoy (€)')
  meta_zona_1 = 10290
  meta_zona_2 = 11986
  meta_zona_3 = 11368
  meta_zona_4 = 14018
  meta_zona_5 = 14036
  meta_zona_6 = 5241
  meta_zona_7 = 3112
  meta_zona_8 = 110
  meta_zona_9 = 7338
  options = {
              "title": {"text": "🍄"},
              "tooltip": {
                  "trigger": "axis",
                  "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
              },
              "legend": {"data": ["Producto_5", "Producto_4", "Producto_3", "Producto_2", "Producto_1"]},
              "toolbox": {"feature": {"saveAsImage": {}}},
              "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
              "xAxis": [
                  {
                      "type": "category",
                      "boundaryGap": False,
                      "data": ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "23:59"],
                  }
              ],
              "yAxis": [{"type": "value"}],
              "series": [
                  {
                      "name": "Producto_5",
                      "type": "line",
                      "stack": "总量",
                      "areaStyle": {},
                      "emphasis": {"focus": "series"},
                      "data": [meta_zona_5*0.1, meta_zona_5*0.2, meta_zona_5*0.35, meta_zona_5*0.45, meta_zona_5*0.5, meta_zona_5*0.75, meta_zona_5],
                  },
                    {
                      "name": "Producto_4",
                      "type": "line",
                      "stack": "总量",
                      "areaStyle": {},
                      "emphasis": {"focus": "series"},
                      "data": [meta_zona_4*0.1, meta_zona_4*0.2, meta_zona_4*0.35, meta_zona_4*0.45, meta_zona_4*0.5, meta_zona_4*0.75, meta_zona_4],
                  },
                    {
                      "name": "Producto_3",
                      "type": "line",
                      "stack": "总量",
                      "areaStyle": {},
                      "emphasis": {"focus": "series"},
                      "data": [meta_zona_3*0.1, meta_zona_3*0.2, meta_zona_3*0.35, meta_zona_3*0.45, meta_zona_3*0.5, meta_zona_3*0.75, meta_zona_3],
                  },
                    {
                      "name": "Producto_2",
                      "type": "line",
                      "stack": "总量",
                      "areaStyle": {},
                      "emphasis": {"focus": "series"},
                      "data": [meta_zona_2*0.1, meta_zona_2*0.2, meta_zona_2*0.35, meta_zona_2*0.45, meta_zona_2*0.5, meta_zona_2*0.75, meta_zona_2],
                  },
                    {
                      "name": "Producto_1",
                      "type": "line",
                      "stack": "总量",
                      "areaStyle": {},
                      "emphasis": {"focus": "series"},
                      "data": [meta_zona_1*0.1, meta_zona_1*0.2, meta_zona_1*0.35, meta_zona_1*0.45, meta_zona_1*0.5, meta_zona_1*0.75, meta_zona_1],
                  },
              ],
          }
  st_echarts(options=options, height="600px")
  
  st.subheader('Costos Financieros en Tasa Efectiva Anual')
  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Socios fundadores", "15%", "5%")
  col2.metric("Nuevos Socios", "14%", "-8%")
  col3.metric("Bonos", "12%", "25%")
  col4.metric("Bancos", "10%", "3%")
  
  st.subheader('Desafíos Comerciales')
  option = {
          "title": {"text": "Eficacia Ventas", "subtext": "Porcentaje Conversión(%)"},
          "tooltip": {"trigger": "item", "formatter": "{a} <br/>{b} : {c}%"},
          "toolbox": {
              "feature": {
                  "dataView": {"readOnly": False},
                  "restore": {},
                  "saveAsImage": {},
              }
          },
          "legend": {"data": ["Contactados", "Interesados", "Persuadidos", "Comprometidos", "Clientes"]},
          "series": [
              {
                  "name": "Contactados",
                  "type": "funnel",
                  "left": "10%",
                  "width": "80%",
                  "label": {"formatter": "{b}%"},
                  "labelLine": {"show": False},
                  "itemStyle": {"opacity": 0.7},
                  "emphasis": {
                      "label": {"position": "inside", "formatter": "{b}预期: {c}%"}
                  },
                  "data": [
                      {"value": 60, "name": "Persuadidos"},
                      {"value": 40, "name": "Comprometidos"},
                      {"value": 20, "name": "Clientes"},
                      {"value": 80, "name": "Interesados"},
                      {"value": 100, "name": "Contactados"},
                  ],
              },
              {
                  "name": "Margen",
                  "type": "funnel",
                  "left": "10%",
                  "width": "80%",
                  "maxSize": "80%",
                  "label": {"position": "inside", "formatter": "{c}%", "color": "#fff"},
                  "itemStyle": {"opacity": 0.5, "borderColor": "#fff", "borderWidth": 2},
                  "emphasis": {
                      "label": {"position": "inside", "formatter": "{b}实际: {c}%"}
                  },
                  "data": [
                      {"value": 30, "name": "Persuadidos"},
                      {"value": 10, "name": "Comprometidos"},
                      {"value": 5, "name": "Clientes"},
                      {"value": 50, "name": "Interesados"},
                      {"value": 80, "name": "Contactados"},
                  ],
                  "z": 100,
              },
          ],
      }
  st_echarts(option, height="500px")     



if a == "Recomendaciones":
  colored_header(
    label="Mando 4: Recomendaciones Operativas, Financieras y Comerciales",
    description="Procesos, Indicadores y Monitoreo",
    color_name="violet-70",
  )
  
  col7, col8, col9 = st.columns(3)
  
  with col7:
      st.write('Oportunidades Operativas 📢')
      with st.expander("Frentes de mayor capacidad de reducción de costos"):
          option = {
              "legend": {},
              "tooltip": {"trigger": "axis", "showContent": False},
              "dataset": {
                  "source": [
                      ["product", "Monday", "Thursday", "Wednesday", "Tuesday", "Friday", "Saturday"],
                      ["Insumos", 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                      ["Personal", 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                      ["Financiación", 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                      ["Energía", 25.2, 37.1, 41.2, 18, 33.9, 49.1],
                  ]
              },
              "xAxis": {"type": "category"},
              "yAxis": {"gridIndex": 0},
              "grid": {"top": "55%"},
              "series": [
                  {
                      "type": "line",
                      "smooth": True,
                      "seriesLayoutBy": "row",
                      "emphasis": {"focus": "series"},
                  },
                  {
                      "type": "line",
                      "smooth": True,
                      "seriesLayoutBy": "row",
                      "emphasis": {"focus": "series"},
                  },
                  {
                      "type": "line",
                      "smooth": True,
                      "seriesLayoutBy": "row",
                      "emphasis": {"focus": "series"},
                  },
                  {
                      "type": "line",
                      "smooth": True,
                      "seriesLayoutBy": "row",
                      "emphasis": {"focus": "series"},
                  },
                  {
                      "type": "pie",
                      "id": "pie",
                      "radius": "30%",
                      "center": ["50%", "25%"],
                      "emphasis": {"focus": "data"},
                      "label": {"formatter": "{b}: {@2012} ({d}%)"},
                      "encode": {"itemName": "product", "value": "Monday", "tooltip": "Monday"},
                  },
              ],
          }
          st_echarts(option, height="500px", key="echarts")
      
  with col8:
      st.write('Oportunidades Financieras 💰')
      with st.expander("Liquidez:"):
          st.subheader('Corto plazo: 1-3 meses')
          st.write('Las mejores tasas se encuentran en el banco X')
          st.subheader('Mediano plazo: 4-12 meses')
          st.write('Las mejores tasas se encuentran en el banco Y')
          
      with st.expander("Endeudamiento:"):
          st.subheader('Con garantía')
          st.write('Las mejores tasas se encuentran en el banco X')
          st.subheader('Sin garantía')
          st.write('Las mejores tasas se encuentran en el banco Y')
          
      with st.expander("Rendimiento:"):
          st.subheader('En Depósitos a Término Fijo')
          st.write('Hasta 10% Efectivo anual')
          st.subheader('En Índices Accionarios')
          st.write('Hasta 15% efectivo anual')
  
  
  with col9:
      st.write('Oportunidades Comerciales 👤')
      with st.expander("Hoy:"):
          st.subheader('Restaurantes')
          st.write('Semana del Rissoto en Valencia')
          
      with st.expander("Mañana:"):
          st.subheader('Restaurantes')
          st.write('Feria Gastronómica en Madrid')
  
      with st.expander("Próxima Semana:"):
          st.subheader('Restaurantes')
          st.write('Inflación Alimenticia mayor en Asturias')
  
  my_grid = grid(3, 3, vertical_align="bottom")
  # Row 1:
  a = my_grid.selectbox("Indica una Producto", ["Producto_1", "Producto_2", "Producto_3", "Producto_4"])
  b = my_grid.selectbox("Indica tipo de Proveedor", ["Personal", "Energía", "Agua", "Herramientas"])
  c = my_grid.selectbox("Indica un Fecha", ["Hoy", "Mañana", "Próxima Semana"])
  
  # Row 2:
  my_grid.button("Activar Recomendación a Equipos en Turno", use_container_width=True)
  my_grid.button("Activar Recomendación a Proveedores", use_container_width=True)
  my_grid.button("Activar Recomendación a Clientes", use_container_width=True)
