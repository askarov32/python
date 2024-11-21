import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
average_max = [0.7, 2.2, 8.7, 17.3, 22.4, 27.5, 30.0, 29.4, 24.2, 16.3, 8.2, 2.3]
average_min = [-8.4, -6.9, -1.1, 5.9, 11.0, 15.8, 18.0, 16.9, 11.5, 4.6, -1.3, -6.4]

data = {
    month: {"avg_max": avg_max, "avg_min": avg_min}
    for month, avg_max, avg_min in zip(months, average_max, average_min)
}

df = pd.DataFrame(data).T

df[['avg_max', 'avg_min']].plot(kind='hist', linewidth=2, rwidth=0.8)
df.plot(kind='hist')
plt.show()

stacked_bar, axis2 = plt.subplots(figsize=(10, 6))
axis2.bar(months, average_max, label="Average High Temp (C)", color='red')
axis2.bar(months, average_min, label="Average Low Temp (C)", bottom=average_max, color='blue')

axis2.set_xlabel("Months")
axis2.set_ylabel("Temperature (°C)")
axis2.set_title("Stacked Monthly High and Low Temperatures")
axis2.legend()

plt.tight_layout()
plt.show()
