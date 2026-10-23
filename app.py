import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configurações Visuais do App
st.set_page_config(page_title="Simulador de Aerodinâmica", layout="wide")

st.title("⛵ Aerodinâmica da Vela: Sustentação e Arrasto")
st.markdown("---")

# Controles na Barra Lateral
st.sidebar.header("⚙️ Ajustes do Vento")
wind_speed = st.sidebar.slider("Velocidade do Vento (m/s)", 0.0, 20.0, 5.0)
sail_angle = st.sidebar.slider("Ângulo da Vela (°)", 0, 90, 30)
bolina = st.sidebar.checkbox("Ativar Bolina", value=True)

# Cálculos de Física
theta = np.radians(sail_angle)
lift = 0.5 * 1.225 * (wind_speed**2) * np.sin(2 * theta) * 0.5
drag = 0.5 * 1.225 * (wind_speed**2) * (np.sin(theta)**2) * 0.2

# Vetores
lx, ly = -lift * np.sin(theta), lift * np.cos(theta)
dx, dy = drag * np.cos(theta), drag * np.sin(theta)
tx, ty = lx + dx, ly + dy

# Desenho do Gráfico
col1, col2 = st.columns([2, 1])

with col1:
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_facecolor('#f0f2f6')
    ax.plot([0, np.cos(theta)*100], [0, np.sin(theta)*100], color='black', lw=5, label="Vela")
    ax.quiver(-150, 0, 100, 0, angles='xy', scale_units='xy', scale=1, color='gray', label="Vento")
    ax.quiver(0, 0, lx, ly, angles='xy', scale_units='xy', scale=1, color='blue', label="Sustentação")
    ax.quiver(0, 0, dx, dy, angles='xy', scale_units='xy', scale=1, color='orange', label="Arrasto")
    ax.quiver(0, 0, tx, ty, angles='xy', scale_units='xy', scale=1, color='green', lw=3, label="Resultante")
    ax.set_xlim(-200, 200); ax.set_ylim(-200, 200); ax.set_aspect('equal')
    ax.legend(); ax.grid(True, alpha=0.3)
    st.pyplot(fig)

with col2:
    st.subheader("📊 Resultados")
    st.metric("Sustentação", f"{lift:.2f} N")
    st.metric("Arrasto", f"{drag:.2f} N")
    if bolina: st.success("Bolina Ativa: Movimento para frente!")
    else: st.error("Sem Bolina: O barco desliza de lado!")