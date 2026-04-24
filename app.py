from flask import Flask, render_template
import pandas as pd
import os

base_dir = "/storage/emulated/0/Lesson/nigeria-dashboard"
app = Flask(__name__, template_folder=os.path.join(base_dir, "templates"))

@app.route('/')
def dashboard():
    file_path = os.path.join(base_dir, "Data/nigeria_gdp_clean.csv")
    nigeria = pd.read_csv(file_path, index_col='Year')

    years = nigeria.index.tolist()
    gdp_values = nigeria['GDP_Growth'].round(2).tolist()

    # Summary stats
    avg_growth = round(nigeria['GDP_Growth'].mean(), 2)
    best_year = nigeria['GDP_Growth'].idxmax()
    worst_year = nigeria['GDP_Growth'].idxmin()
    best_value = round(nigeria['GDP_Growth'].max(), 2)
    worst_value = round(nigeria['GDP_Growth'].min(), 2)
    latest_year = years[-1]
    latest_value = gdp_values[-1]

    # Recession & Boom years
    recession_years = nigeria[nigeria['GDP_Growth'] < 0].index.tolist()
    boom_years = nigeria[nigeria['GDP_Growth'] > 5].index.tolist()

    # Decade averages
    nigeria_copy = nigeria.copy()
    nigeria_copy['Decade'] = [str(int(y) // 10 * 10) + 's' for y in years]
    decade_avg = nigeria_copy.groupby('Decade')['GDP_Growth'].mean().round(2)
    best_decade = decade_avg.idxmax()
    worst_decade = decade_avg.idxmin()

    # Insights
    insights = [
        f"Nigeria's economy grew at an average of {avg_growth}% per year over 64 years.",
        f"The best single year was {best_year} with {best_value}% growth, likely driven by post-civil war reconstruction.",
        f"The worst year was {worst_year} with {worst_value}% growth, reflecting the oil price crash.",
        f"Nigeria experienced {len(recession_years)} recession years out of 64 recorded years.",
        f"The {best_decade} decade was the strongest, while the {worst_decade} decade was the weakest on average.",
        f"In {latest_year}, Nigeria's GDP growth stood at {latest_value}%, showing recent economic performance."
    ]

    # Recommendations
    recommendations = [
        "Diversify beyond oil — most recession years align with global oil price crashes.",
        "Invest in agriculture and tech sectors which showed resilience during downturns.",
        "Strengthen foreign reserves to buffer against commodity price shocks.",
        "Encourage local manufacturing to reduce import dependency and boost GDP stability.",
        "Improve infrastructure to attract foreign direct investment and sustain growth above 5%."
    ]

    return render_template('index.html',
        years=years,
        gdp_values=gdp_values,
        avg_growth=avg_growth,
        best_year=best_year,
        worst_year=worst_year,
        best_value=best_value,
        worst_value=worst_value,
        latest_year=latest_year,
        latest_value=latest_value,
        recession_count=len(recession_years),
        boom_count=len(boom_years),
        best_decade=best_decade,
        worst_decade=worst_decade,
        insights=insights,
        recommendations=recommendations
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)