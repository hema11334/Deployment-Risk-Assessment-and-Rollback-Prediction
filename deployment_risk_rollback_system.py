

from sklearn.ensemble import RandomForestClassifier

X = [[50, 1], [200, 0], [30, 1], [150, 0], [20, 1]]
y = [0, 1, 0, 1, 0]  # 1 = rollback, 0 = success

model = RandomForestClassifier()
model.fit(X, y)

def predict_rollback(change_size, time_of_day):
    return model.predict([[change_size, time_of_day]])[0]

import random

def get_metrics():
    error_rate = random.uniform(0, 1)
    cpu_usage = random.randint(20, 95)
    return error_rate, cpu_usage

def perform_rollback():
    print(" ROLLBACK TRIGGERED: Restoring previous stable version...")

import time

print(" Starting Deployment...")

change_size = 120
time_of_day = 0

risk = predict_rollback(change_size, time_of_day)
if risk == 1:
    print(" High rollback risk detected before deployment.")
else:
    print(" Deployment risk is low. Proceeding...")

print("\n Monitoring system...")
for i in range(3):
    error, cpu = get_metrics()
    print(f"Check {i+1}  Error Rate: {error:.2f}, CPU: {cpu}%")
    time.sleep(1)

    if error > 0.5 or cpu > 80:
        perform_rollback()
        break
else:
    print(" Deployment stable. No rollback needed.")
