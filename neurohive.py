print("===================================")
print("        NEUROHIVE AI SYSTEM")
print("===================================")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
study_hours = float(input("Enter your daily study hours: "))
stress_level = int(input("Enter your stress level (1-10): "))
sleep_hours = float(input("Enter your sleep hours: "))

print("\n--- NEUROHIVE ANALYSIS ---")

score = 0

# Study analysis
if study_hours >= 6:
    score += 30
    study_status = "Excellent"
elif study_hours >= 4:
    score += 20
    study_status = "Good"
else:
    score += 10
    study_status = "Needs Improvement"

# Sleep analysis
if sleep_hours >= 7:
    score += 25
    sleep_status = "Healthy"
elif sleep_hours >= 5:
    score += 15
    sleep_status = "Moderate"
else:
    score += 5
    sleep_status = "Low"

# Stress analysis
if stress_level <= 3:
    score += 25
    stress_status = "Low Stress"
elif stress_level <= 6:
    score += 15
    stress_status = "Moderate Stress"
else:
    score += 5
    stress_status = "High Stress"

# Overall recommendation
if score >= 70:
    recommendation = "Your daily routine is balanced. Keep going!"
elif score >= 50:
    recommendation = "Your routine is moderate. Improve sleep and study consistency."
else:
    recommendation = "You need to improve your daily routine and reduce stress."

print("\nName:", name)
print("Age:", age)

print("\nStudy Status:", study_status)
print("Sleep Status:", sleep_status)
print("Stress Status:", stress_status)

print("\nNEUROHIVE Score:", score, "/ 80")
print("Recommendation:", recommendation)

print("\n===================================")
print("       ANALYSIS COMPLETED")
print("===================================")
