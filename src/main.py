import pandas as pd
import plotly.express as px
import requests


def get_spy_heatmap(date: str = "one_day") -> pd.DataFrame:
    """
    Fetches the S&P 500 heatmap data from Unusual Whales API.

    Parameters
    ----------
    date : str, optional
        Options are: one_day, after_hours, yesterday, one_week, one_month, ytd, one_year, by default "one_day"

    Returns
    -------
    pd.DataFrame
        The S&P 500 heatmap data as a DataFrame.
    """
    data = requests.get(
        f"https://phx.unusualwhales.com/api/etf/SPY/heatmap?date_range={date}",
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
        },
    ).json()

    # Create DataFrame
    df = pd.DataFrame(data["data"])

    # Convert relevant columns to numeric types
    df["call_premium"] = pd.to_numeric(df["call_premium"])
    df["close"] = pd.to_numeric(df["close"])
    df["high"] = pd.to_numeric(df["high"])
    df["low"] = pd.to_numeric(df["low"])
    df["marketcap"] = pd.to_numeric(df["marketcap"])
    df["open"] = pd.to_numeric(df["open"])
    df["prev_close"] = pd.to_numeric(df["prev_close"])
    df["put_premium"] = pd.to_numeric(df["put_premium"])

    # Add change column
    df["percentage_change"] = (df["close"] - df["prev_close"]) / df["prev_close"] * 100

    # Drop rows where the marketcap == 0
    df = df[df["marketcap"] > 0]

    return df


def create_treemap(df: pd.DataFrame, save_img: bool = True) -> None:
    """
    Creates a treemap of the S&P 500 heatmap data.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame containing the S&P 500 heatmap data.
    save_img : bool, optional
        Saves the heatmap as a image, by default False
    """

    # Custom color scale
    color_scale = [
        (0, "#ff2c1c"),  # Bright red at -5%
        (0.5, "#484454"),  # Grey around 0%
        (1, "#30dc5c"),  # Bright green at 5%
    ]

    # Generate the treemap
    fig = px.treemap(
        df,
        path=[px.Constant("Sectors"), "sector", "industry", "ticker"],
        values="marketcap",
        color="percentage_change",
        hover_data=["percentage_change", "ticker", "marketcap"],
        color_continuous_scale=color_scale,
        range_color=(-5, 5),
        color_continuous_midpoint=0,
    )

    # Removes background colors to improve saved image
    fig.update_layout(
        margin=dict(t=30, l=10, r=10, b=10),
        font_size=20,
        coloraxis_colorbar=None,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    fig.data[0].texttemplate = "%{customdata[1]}<br>%{customdata[0]:.2f}%"

    # Set the text position to the middle of the treemap
    # and add a black border around each box
    fig.update_traces(
        textposition="middle center",
        marker=dict(line=dict(color="black", width=1)),
    )

    # Disable the color bar
    fig.update(layout_coloraxis_showscale=False)

    # Save the figure as an image
    # Increase the width and height for better quality
    if save_img:
        fig.write_image(
            file="img/spy_heatmap.png", format="png", width=1920, height=1080
        )

    # Plot the figure
    fig.show()


if __name__ == "__main__":
    create_treemap(get_spy_heatmap())
