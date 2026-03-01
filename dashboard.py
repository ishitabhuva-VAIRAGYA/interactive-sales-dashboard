
# Interactive Sales Dashboard


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load dataset
df = pd.read_csv("sales_data.csv")


# SEABORN VISUALIZATIONS


sns.set_theme(style="whitegrid", palette="viridis")

# 1. Box Plot - Sales Distribution by Category
plt.figure(figsize=(8,5))
sns.boxplot(x='Category', y='Sales', data=df)
plt.title("Sales Distribution by Category")
plt.tight_layout()
plt.savefig("visualizations/boxplot.png")
plt.close()

# 2. Violin Plot - Customer Segment Sales
plt.figure(figsize=(8,5))
sns.violinplot(x='Segment', y='Sales', data=df)
plt.title("Sales by Customer Segment")
plt.tight_layout()
plt.savefig("visualizations/violinplot.png")
plt.close()

# 3. Correlation Heatmap
plt.figure(figsize=(6,5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visualizations/heatmap.png")
plt.close()

# 4. Bar Plot - Product Performance
plt.figure(figsize=(8,5))
sns.barplot(x='Product', y='Sales', data=df)
plt.xticks(rotation=45)
plt.title("Product Performance")
plt.tight_layout()
plt.savefig("visualizations/barplot.png")
plt.close()

# -------------------------------
# PLOTLY INTERACTIVE DASHBOARD
# -------------------------------

# 5. Interactive Sales Trend
fig_trend = px.line(
    df,
    x="Date",
    y="Sales",
    title="Interactive Sales Trend",
    markers=True,
    hover_data=['Product', 'Category']
)

# 6. Interactive Pie Chart - Customer Segmentation
fig_pie = px.pie(
    df,
    names="Segment",
    values="Sales",
    title="Customer Segmentation"
)

# 7. Combined Dashboard Layout
dashboard = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Sales Trend", "Customer Segmentation",
                    "Category Performance", "Regional Sales"),
    specs=[[{"type": "scatter"}, {"type": "domain"}],
           [{"type": "bar"}, {"type": "bar"}]]
)

dashboard.add_trace(
    go.Scatter(x=df["Date"], y=df["Sales"], mode='lines+markers'),
    row=1, col=1
)

dashboard.add_trace(
    go.Pie(labels=df["Segment"], values=df["Sales"]),
    row=1, col=2
)

dashboard.add_trace(
    go.Bar(x=df["Category"], y=df["Sales"]),
    row=2, col=1
)

dashboard.add_trace(
    go.Bar(x=df["Region"], y=df["Sales"]),
    row=2, col=2
)

dashboard.update_layout(
    height=800,
    width=1000,
    title_text="Interactive Sales Dashboard",
    template="plotly_dark"
)

dashboard.write_html("dashboard.html")

print("Dashboard created successfully!")