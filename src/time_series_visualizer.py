import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
script_dir = os.path.dirname(__file__)
data_dir = os.path.join(script_dir[:-3], "data/fcc-forum-pageviews.csv")
output_dir = os.path.join(script_dir[:-3], "output")

df = pd.read_csv(data_dir, encoding="utf-8")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

# Clean data
df = df.drop(df[(df["value"] < df["value"].quantile(0.025)) | (df["value"] > df["value"].quantile(0.975))].index)


def draw_line_plot():
    # Draw line plot
    fig, axes = plt.subplots(figsize=(32, 10), dpi=100)
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    axes.set_xlabel("Date")
    axes.set_ylabel("Page Views")
    sns.lineplot(data=df, legend=False, color="red")

    # Save image and return fig (don't change this part)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    fig.savefig(output_dir + "/line_plot.png")

    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Year"] = pd.DatetimeIndex(df_bar.index).year
    df_bar["Month"] = pd.DatetimeIndex(df_bar.index).month

    df_bar = df_bar.groupby(["Year", "Month"])["value"].mean()
    df_bar = df_bar.unstack()
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    # Draw bar plot
    fig = df_bar.plot(kind="bar", figsize=(15, 10)).figure

    plt.title("")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    lg = plt.legend(title="Months", fontsize=15, labels=month_names)
    title = lg.get_title()
    title.set_fontsize(15)

    # Save image and return fig (don't change this part)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    fig.savefig(output_dir + "/bar_plot.png")

    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(32, 10), dpi=100)

    # Yearly boxplot
    sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Monthly boxplot
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=months, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    fig.savefig(output_dir + "/box_plot.png")

    return fig
