import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def create_dashboard(daily, weekly, summary, save_path='output/dashboard.png'):
    fig, axs = plt.subplots(3,1, figsize=(14,16))

    axs[0].plot(daily.index, daily.values)
    axs[0].set_title("Daily Energy Consumption")

    axs[1].bar(weekly.index, weekly.values)
    axs[1].set_title("Weekly Avg Consumption")

    axs[2].scatter(summary['mean'], summary['total_kwh'])
    axs[2].set_xlabel("Mean kWh")
    axs[2].set_ylabel("Total kWh")
    axs[2].set_title("Mean vs Total Consumption")

    plt.tight_layout()
    plt.savefig(save_path)
    print("Dashboard saved.")
