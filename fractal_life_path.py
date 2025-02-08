import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def generate_life_fractal(nexus_points, title="Fractal-Inspired Life Path"):
    """
    Generates a fractal-like visualization of life path coordinates.
    
    Parameters:
    - nexus_points: Dictionary of key life events and their (x, y) coordinates.
    - title: Title of the visualization.
    """
    # Extract coordinates
    x_values = [coord[0] for coord in nexus_points.values()]
    y_values = [coord[1] for coord in nexus_points.values()]
    labels = list(nexus_points.keys())

    # Create plot
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the main points
    ax.scatter(x_values, y_values, color="blue", s=100, label="Nex-(to)-Us Points")

    # Draw connecting lines using a recursive pattern (approximating fractal growth)
    for i in range(len(x_values)):
        for j in range(i + 1, len(x_values)):
            ax.plot([x_values[i], x_values[j]], [y_values[i], y_values[j]], "gray", alpha=0.3)

    # Annotate points
    for label, (x, y) in nexus_points.items():
        ax.text(x, y, label, fontsize=10, ha="right")

    # Formatting
    ax.set_title(title)
    ax.set_xlabel("Spatial/Experiential Dimension")
    ax.set_ylabel("Temporal/Emotional Dimension")
    ax.grid(True)

    return fig

# Streamlit App
st.title("Fractal Life Path Generator")
st.write("Map your life's journey through Nex-(to)-Us points!")

# User input for life events
nexus_points = {}
num_points = st.number_input("How many key life events do you want to map?", min_value=2, max_value=20, value=5)

for i in range(num_points):
    label = st.text_input(f"Event {i+1} Name:", value=f"Event {i+1}")
    x = st.slider(f"X-Coordinate for {label}", -10, 10, 0)
    y = st.slider(f"Y-Coordinate for {label}", -10, 10, 0)
    nexus_points[label] = (x, y)

# Generate and display visualization
if st.button("Generate Fractal Path"):
    fig = generate_life_fractal(nexus_points, title="Your Fractal Life Path")
    st.pyplot(fig)

# Instructions for Deployment
st.markdown("""
### Deployment Instructions:
1. **Set Up a GitHub Repository**
   - Upload this Python script as `fractal_life_path.py`
   - Add `requirements.txt` with:
     ```
     streamlit
     matplotlib
     numpy
     ```

2. **Deploy to Streamlit Cloud**
   - Go to [Streamlit Community Cloud](https://share.streamlit.io).
   - Click **"New App"**, connect to your GitHub repo, and select `fractal_life_path.py`.

3. **Enhancements (Optional)**
   - 🎨 Custom themes for a better UI
   - 📂 File upload to add previous life events
   - 🔄 3D visualization for deeper insights
""")
