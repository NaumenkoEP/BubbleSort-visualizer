# type: ignore
import streamlit as st
import matplotlib.pyplot as plt
import time

class SortingVisualizer:
    def __init__(self):
        self.data = []

    def draw_bars(self, data, highlight=[]):
        """Draws the bars for visualization with optional highlights."""
        fig, ax = plt.subplots()
        colors = ["red" if i in highlight else "green" for i in range(len(data))]
        ax.bar(range(len(data)), data, color=colors)
        ax.set_ylim(0, max(data) + 5)
        return fig

    def bubble_sort(self, data):
        """Performs bubble sort step-by-step and saves frames."""
        steps = []
        n = len(data)
        for i in range(n):
            for j in range(n - i - 1):
                steps.append((data.copy(), [j, j + 1])) 
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        steps.append((data.copy(), [])) 
        return steps


st.title("Bubble Sort Visualizer")

user_input = st.text_input("Enter numbers separated by spaces")

if st.button("Start Sorting"):
    try:
        data = list(map(int, user_input.split()))
        if len(data) < 2:
            st.error("Please enter at least two numbers.")
        else:
            visualizer = SortingVisualizer()
            steps = visualizer.bubble_sort(data)

            plot_placeholder = st.empty()

            for step_data, highlight in steps:
                fig = visualizer.draw_bars(step_data, highlight)
                plot_placeholder.pyplot(fig) 
                time.sleep(0.1)  

    except ValueError:
        st.error("Invalid input! Please enter numbers separated by spaces.")
