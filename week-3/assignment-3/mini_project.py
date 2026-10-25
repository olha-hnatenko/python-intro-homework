day_of_week = input("What day is it? ")
time_of_day = input("Enter the time of day (morning, afternoon, evening): ")

if day_of_week.lower() == "monday" and time_of_day.lower() == "morning":
    print("Don't forget to have breakfast.")
elif day_of_week.lower() == "monday" and time_of_day.lower() == "afternoon":
    print("Take a short walk after lunch.")
elif day_of_week.lower() == "monday" and time_of_day.lower() == "evening":
    print("Plan your tasks for tomorrow.")
elif day_of_week.lower() == "wednesday" and time_of_day.lower() == "morning":
    print("Start your day with a healthy breakfast.")
elif day_of_week.lower() == "wednesday" and time_of_day.lower() == "afternoon":
    print("Take a lunch break away from your phone.")
elif day_of_week.lower() == "wednesday" and time_of_day.lower() == "evening":
    print("Review your tasks for the day.")
elif day_of_week.lower() == "saturday" and time_of_day.lower() == "morning":
    print("Enjoy your weekend morning!")
elif day_of_week.lower() == "saturday" and time_of_day.lower() == "afternoon":
    print("Relax and have fun this afternoon.")
elif day_of_week.lower() == "saturday" and time_of_day.lower() == "evening":
    print("Spend your evening with loved ones.")
else:
    print("Enter your answers correctly!")  