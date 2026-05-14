import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

# Configuración de página
st.set_page_config(page_title="Elite Scouting System", page_icon="⚽", layout="wide")

# Estilos CSS
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: bold; color: #1E88E5; margin-bottom: 0px; }
    .sub-header { font-size: 1.2rem; color: #757575; margin-bottom: 30px; }
</style>
""", unsafe_allow_html=True)

# Título Principal
st.markdown('<div class="main-header">⚽ Elite Scouting System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Data-Driven Player Recruitment Dashboard</div>', unsafe_allow_html=True)

# Cargar Datos
@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "players_data.csv")
    df = pd.read_csv(file_path)
    return df

df = load_data()

# Features for comparison
features = ['Goles', 'Asistencias', 'Pases_%', 'Regates', 'Recuperaciones', 'Duelos_Aereos', 'xG']




#  SIDEBAR 
st.sidebar.header("⚙️ Panel de Control")

# Target Player Selection
target_player_name = st.sidebar.selectbox("🎯 Jugador Objetivo", df['Nombre'].tolist(), index=0)
target_player = df[df['Nombre'] == target_player_name].iloc[0]

# Search Priority
search_priority = st.sidebar.radio("🔍 Prioridad de Búsqueda", ["Similitud Actual", "Potencial Juvenil"])

# Filters
st.sidebar.subheader("Filtros")
max_age = st.sidebar.slider("Edad Máxima", 16, 40, 25)
max_budget = st.sidebar.number_input("Presupuesto Máximo (M€)", min_value=0, max_value=300, value=150, step=10)

# LOGIC 
# Normalize data manually (MinMax)
df_normalized = df.copy()
for col in features:
    min_val = df[col].min()
    max_val = df[col].max()
    if max_val != min_val:
        df_normalized[col] = (df[col] - min_val) / (max_val - min_val)
    else:
        df_normalized[col] = 0

target_normalized = df_normalized[df_normalized['Nombre'] == target_player_name][features].iloc[0].values




# Calculate Similarity Score (Euclidean distance converted to a 0-100 score)
def calculate_similarity(row):
    dist = np.sqrt(np.sum((target_normalized - row[features].values)**2))
    max_dist = np.sqrt(len(features))
    score = max(0, 100 - (dist / max_dist) * 100)
    return score

df['Similarity_Score'] = df_normalized.apply(calculate_similarity, axis=1)




# Filter Candidates
candidates = df[
    (df['Nombre'] != target_player_name) & 
    (df['Edad'] <= max_age) & 
    (df['Valor_Mercado'] <= max_budget)
].copy()

if search_priority == "Similitud Actual":
    candidates = candidates.sort_values(by='Similarity_Score', ascending=False)
else:
    candidates = candidates.sort_values(by=['Potencial', 'Similarity_Score'], ascending=[False, False])

top_candidates = candidates.head(10)

#MAIN PANEL


col1, col2 = st.columns([1, 1])

with col1:
    st.subheader(f"📊 Perfil Estadístico: {target_player_name}")
    # Radar Chart
    fig_radar_target = go.Figure()
    fig_radar_target.add_trace(go.Scatterpolar(
        r=target_player[features].tolist() + [target_player[features].tolist()[0]], 
        theta=features + [features[0]],
        fill='toself',
        name=target_player_name,
        line_color='#1E88E5'
    ))
    fig_radar_target.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, df[features].max().max()])),
        showlegend=False,
        margin=dict(l=40, r=40, t=20, b=20)
    )
    st.plotly_chart(fig_radar_target, use_container_width=True)

with col2:
    st.subheader("🗺️ Posicionamiento Táctico")



    fig_scatter = px.scatter(
        df, x='Coord_X_Media', y='Coord_Y_Media', 
        color='Valor_Mercado', hover_name='Nombre',
        labels={'Coord_X_Media': 'Amplitud', 'Coord_Y_Media': 'Profundidad'},
        color_continuous_scale='Viridis'
    )



    fig_scatter.add_trace(go.Scatter(
        x=[target_player['Coord_X_Media']], y=[target_player['Coord_Y_Media']],
        mode='markers', marker=dict(color='red', size=15, symbol='star'),
        name=target_player_name, showlegend=False, hoverinfo='skip'
    ))
    st.plotly_chart(fig_scatter, use_container_width=True)

st.subheader("📋 Candidatos Identificados")
display_cols = ['Nombre', 'Equipo', 'Edad', 'Valor_Mercado', 'Potencial', 'Similarity_Score']
st.dataframe(
    top_candidates[display_cols].style.format({'Similarity_Score': '{:.1f}%'}),
    use_container_width=True,
    hide_index=True
)

# TECHNICAL COMPARISON
st.markdown("---")
st.header("⚖️ Comparativa Técnica")

if not top_candidates.empty:
    selected_candidate_name = st.selectbox("Seleccionar Candidato para Comparar", top_candidates['Nombre'].tolist())
    candidate = top_candidates[top_candidates['Nombre'] == selected_candidate_name].iloc[0]
    
    col3, col4 = st.columns([1, 1])
    
    with col3:
        st.subheader("Comparativa Radar")
        fig_comp = go.Figure()
        
        # Target
        fig_comp.add_trace(go.Scatterpolar(
            r=target_player[features].tolist() + [target_player[features].tolist()[0]],
            theta=features + [features[0]],
            fill='toself',
            name=target_player_name,
            line_color='#1E88E5'
        ))
        
        # Candidate
        fig_comp.add_trace(go.Scatterpolar(
            r=candidate[features].tolist() + [candidate[features].tolist()[0]],
            theta=features + [features[0]],
            fill='toself',
            name=selected_candidate_name,
            line_color='#FF5252'
        ))
        
        fig_comp.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, df[features].max().max()])),
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_comp, use_container_width=True)
        
    with col4:
        st.subheader("📈 Proyección de Crecimiento (2024-2027)")
        years = [2024, 2025, 2026, 2027]
        
        def calculate_projection(player, years):
            base_overall = np.mean([df_normalized[df_normalized['Nombre'] == player['Nombre']][f].values[0] for f in features]) * 100 
            potential = player['Potencial']
            age = player['Edad']
            growth_rate = max(0, (potential - base_overall) / max(1, (28 - age))) if age < 28 else -1
            
            proj = []
            current = base_overall
            for y in years:
                proj.append(current)
                if current < potential:
                    current += growth_rate
                else:
                    current = potential
            return proj
            
        target_proj = calculate_projection(target_player, years)
        candidate_proj = calculate_projection(candidate, years)
        
        fig_growth = go.Figure()
        fig_growth.add_trace(go.Scatter(x=years, y=target_proj, mode='lines+markers', name=target_player_name, line=dict(color='#1E88E5', width=3)))
        fig_growth.add_trace(go.Scatter(x=years, y=candidate_proj, mode='lines+markers', name=selected_candidate_name, line=dict(color='#FF5252', width=3, dash='dash')))
        
        fig_growth.update_layout(
            xaxis=dict(tickvals=years),
            yaxis_title="Índice de Rendimiento Estimado",
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_growth, use_container_width=True)
else:
    st.info("Ningún candidato cumple con los filtros actuales.")