import dash
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

rpm_bar = daq.GraduatedBar(
    id="rpm_bar",
    min=0,
    max=7000,  # max rpm
    step=140,  # hist bin width
    color={
        "gradient": True,
        "ranges": {
            # "green": [0, 2000],
            "yellow": [0, 5000],
            "orange": [5000, 6000],
            "red": [6000, 7000],
        },
    },
    showCurrentValue=False,
    value=3500,
)

rpm_slider = dcc.Slider(
    id="my-graduated-bar-slider-1",
    min=0,
    max=7000,
    step=70,
    value=3500,  # slider bar steps
)

rpm_numeric = daq.LEDDisplay(
    label={
        "label": "RPM",
        "style": {"size": 100},  # Need to be able to change this size
    },
    size=20,
    value=3500,
    color="#FF5E5E",
)

speedometer = daq.Gauge(
    label="Speed",
    scale={"start": 0, "interval": 5, "labelInterval": 4},
    color={
        "gradient": False,
        "ranges": {"black": [0, 150], "red": [150, 160]},
    },
    value=65,
    max=160,
    min=0,
)

app = dash.Dash(__name__)
app.layout = html.Div([rpm_bar, rpm_slider, rpm_numeric, speedometer])


@app.callback(Output("rpm_bar", "value"), Input("my-graduated-bar-slider-1", "value"))
def update_output(value):
    return value


if __name__ == "__main__":
    app.run_server(debug=True)
