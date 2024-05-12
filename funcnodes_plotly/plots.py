from typing import List, Literal, Optional, Any, Tuple
import plotly.graph_objects as go
import funcnodes as fn


class ColorScale(fn.DataEnum):
    Viridis = "Viridis"
    Cividis = "Cividis"
    Inferno = "Inferno"
    Magma = "Magma"
    Plasma = "Plasma"
    Turbo = "Turbo"
    Jet = "Jet"
    Hot = "Hot"
    Blackbody = "Blackbody"
    Earth = "Earth"
    Electric = "Electric"
    Rainbow = "Rainbow"
    Picnic = "Picnic"
    Portland = "Portland"
    YlGnBu = "YlGnBu"
    YlOrRd = "YlOrRd"
    Bluered = "Bluered"
    RdBu = "RdBu"
    Reds = "Reds"
    Blues = "Blues"


@fn.NodeDecorator(
    "plotly.make_scatter",
    name="Make Scatter Plot",
    default_io_options={
        "opacity": {"value_options": {"min": 0, "max": 1, "step": 0.01}},
    },
    default_render_options={
        "io": {
            "c": {"type": "color"},
        },
    },
)
def make_scatter(
    y: List[float],
    x: Optional[List[float]] = None,
    mode: Literal["lines", "markers", "lines+markers"] = "lines+markers",
    name: Optional[str] = None,
    c: Optional[str] = None,
    opacity: float = 1,
) -> go.Scatter:
    """
    Create a scatter plot with the given x and y values.

    Parameters
    ----------
    y : List[float]
        The y values of the scatter plot.
    x : Optional[List[float]], optional
        The x values of the scatter plot, by default None. If None, the x values will be the indices of the y values.
    mode : Literal["lines", "markers", "lines+markers"], optional
        The mode of the scatter plot, by default "lines+markers".
    figure : Optional[go.Figure], optional
        The figure object to add the scatter plot to, by default None.


    Returns
    -------
    go.Scatter
        The scatter plot object.
    """
    d = {
        "x": x,
        "y": y,
        "mode": mode,
        "opacity": opacity,
        "marker": {},
        "line": {},
    }
    if name is not None:
        d["name"] = name
    if c is not None:
        if not c.startswith("#"):
            c = "#" + c
        d["marker"]["color"] = c
        d["line"]["color"] = c
    return go.Scatter(**d)


@fn.NodeDecorator(
    "plotly.make_bar",
    name="Make Bar Plot",
    default_io_options={
        "opacity": {"value_options": {"min": 0, "max": 1, "step": 0.01}},
    },
    default_render_options={
        "io": {
            "c": {"type": "color"},
        },
    },
)
def make_bar(
    y: List[float],
    x: Optional[List[float]] = None,
    name: Optional[str] = None,
    c: Optional[str] = None,
    opacity: float = 1,
) -> go.Bar:
    """
    Create a bar plot with the given x and y values.

    Parameters
    ----------
    y : List[float]
        The y values of the bar plot.
    x : Optional[List[float]], optional
        The x values of the bar plot, by default None. If None, the x values will be the indices of the y values.

    Returns
    -------
    go.Bar
        The bar plot object.
    """
    d = {
        "x": x,
        "y": y,
        "opacity": opacity,
    }
    if name is not None:
        d["name"] = name
    if c is not None:
        if not c.startswith("#"):
            c = "#" + c
        d["marker"] = {"color": c}
    return go.Bar(**d)


@fn.NodeDecorator("plotly.make_heatmap", name="Make Heatmap Plot")
def make_heatmap(
    z: List[List[float]],
    x: Optional[List[Any]] = None,
    y: Optional[List[Any]] = None,
    c: ColorScale = ColorScale.Viridis,
) -> go.Heatmap:
    """
    Create a heatmap plot with the given z values.

    Parameters
    ----------
    z : List[List[float]]
        The z values of the heatmap plot.
    x : Optional[List[Any]], optional
        The x values of the heatmap plot, by default None. If None, the x values will be the indices of the z values.
    y : Optional[List[Any]], optional
        The y values of the heatmap plot, by default None. If None, the y values will be the indices of the z values.

    Returns
    -------
    go.Heatmap
        The heatmap plot object.
    """
    c = ColorScale.v(c)

    return go.Heatmap(
        x=x,
        y=y,
        z=z,
        hoverongaps=False,
        colorscale=c,
    )


NODE_SHELF = fn.Shelf(
    nodes=[
        make_scatter,
        make_bar,
        make_heatmap,
    ],
    name="Plots",
    description="A collection of functions for creating plotly traces.",
    subshelves=[],
)
