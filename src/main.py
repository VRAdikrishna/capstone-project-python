import os
os.makedirs("output", exist_ok=True)

from src.ingestion import load_and_validate_data
from src.aggregation import calculate_daily_totals, calculate_weekly_aggregates, building_wise_summary
from src.visualization import create_dashboard

def main():
    df = load_and_validate_data('data/')
    df.to_csv('output/cleaned_energy_data.csv', index=False)

    daily = calculate_daily_totals(df)
    weekly = calculate_weekly_aggregates(df)
    summary = building_wise_summary(df)

    summary.to_csv('output/building_summary.csv')

    create_dashboard(daily, weekly, summary)

    total = df['kwh'].sum()
    highest = summary['total_kwh'].idxmax()
    peak = df.groupby(df['timestamp'].dt.hour)['kwh'].sum().idxmax()

    with open('output/summary.txt','w') as f:
        f.write("CAMPUS ENERGY SUMMARY\n")
        f.write(f"Total Campus Consumption: {total} kWh\n")
        f.write(f"Highest Consuming Building: {highest}\n")
        f.write(f"Peak Load Hour: {peak}:00 hrs\n")

    print("Summary exported.")

if __name__ == "__main__":
    main()
