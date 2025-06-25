#Example 1:Greeting message for Morning
#Input: 9 AM
#output: "Good Morning!"

#Example 2:Greeting message for Afternoon
#Input: 2 PM
#output: "Good Afternoon!"

#Example 2:Greeting message for Evening
#Input: 7 PM
#output: "Good Evening!"

#Now Generate python code that takes current time as input using datetime module
# and returns appropriate greeting message based on the time of day.

from datetime import datetime

def get_greeting_message():
    """
    Returns a greeting message based on the current time of day.
    
    Returns:
        str: Greeting message ("Good Morning!", "Good Afternoon!", or "Good Evening!").
    """
    current_time = datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 17:
        return "Good Afternoon!"
    else:
        return "Good Evening!"