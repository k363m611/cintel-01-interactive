from shiny import App, Inputs, Outputs, Session, ui, render
import matplotlib.pyplot as plt
import numpy as np
import shinyswatch

app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.style("""
            .title-box {
                background-color: #A4C3B2;
                border: 1px solid #ccc;
                padding: 10px;
                text-align: center;
                font-family: 'Arial', sans-serif;
                font-size: 20px;
                color: #000000;
                margin-bottom: 20px;
                border-radius: 9px;
            }
        """)
    ),
    ui.div(
        ui.panel_title("Katie's Shiny Histogram-randomized data"),
        class_="title-box"
    ),
    ui.page_fillable(
        ui.card(
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20),
                    bg="#F6FFF8"
                ),   
                ui.output_plot("histogram")
            ),
            ui.card_header("Module 1 Project for Continuous Intelligence & Interactive Analytics"),
        )
    ),
    theme=shinyswatch.theme.minty
)

def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.plot(alt="A histogram")
    def histogram():
        np.random.seed(19680801)
        x = 100 + 15 * np.random.randn(437)
        plt.hist(x, bins=input.selected_number_of_bins(), density=True, color="#6B9080")  # Access using the new ID
        plt.xlabel("Value")
        plt.ylabel("Density")
        plt.title("Histogram with Randomized Data")

app = App(app_ui, server)