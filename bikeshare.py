import time
import pandas as pd

# Colors to style text
FONT_CYAN = "\033[36m"
FONT_BLACK = "\033[30m"
FONT_MAGENTA = "\033[35m"
BOLD = "\033[1m"
BACK_MAGENTA = "\033[45m"
BACK_WHITE = "\033[47m"
ITALIC = "\x1B[3m"
ITALIC_OFF = "\x1B[0m"
REVERSE = "\033[7m"
UNDERSCORE = "\033[4m"
ALL_OFF = "\033[0m"

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze

        (int) month - name of the month to filter by, or None  to apply no month filter
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June"

        (int) day - number of the day of week to filter by, or None to apply no day filter
        0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"
    """


    # functions
    def month_filter():
        #Aask for month
        print("Which month? \n"
              "- January\n- February\n- March\n- April\n- May\n- June\n")
        chosen_month_raw = input(" -> Your input: ")
        chosen_month = chosen_month_raw.upper()

        # dictionary to control the input
        month_str = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE"]
        # dictionary to convert the string month into int
        month_dict = {"JANUARY": 1, "FEBRUARY": 2, "MARCH": 3, "APRIL": 4, "MAY": 5, "JUNE": 6}

        #input control
        while chosen_month not in month_str:
            print("Please enter a valid month:\n"
                  "- January\n- February\n- March\n- April\n- May\n- June\n")
            chosen_month_raw = input(" -> Your input: ")
            chosen_month = chosen_month_raw.upper()

        month = month_dict.get(chosen_month)

        return month

    def day_filter():
        print("Which day?\n- Sunday\n- Monday\n- Tuesday\n- Wednesday\n- Thursday\n- Friday\n- Saturday\n")
        chosen_day_raw = input(" -> Your input: ")
        chosen_day = chosen_day_raw.upper()

        # dictionary to control the input
        day_str = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
        # dictionary to convert day str into int
        day_dict = {"SUNDAY": 0, "MONDAY": 1, "TUESDAY": 2, "WEDNESDAY": 3, "THURSDAY": 4, "FRIDAY": 5, "SATURDAY": 6}

        # input control
        while chosen_day not in day_str:
            print("Please enter a valid day. \n- Sunday\n- Monday\n- Tuesday\n- Wednesday\n- Thursday\n- Friday\n- Saturday\n")
            chosen_day_raw = input(" -> Your input: ")
            chosen_day = chosen_day_raw.upper()

        day = day_dict.get(chosen_day)

        return day

    """program starts"""
    # Intro text
    print(FONT_CYAN + BOLD + "Hello, welcome to the US bikesharing data-explorer!")
    print("This program will guide you through the available data. Please follow the instructions:" + "\033[0m")
    print('-' * 40)
    print(" ")

    # city flow
    print(BOLD + "Which city would you like to explore?:" + ALL_OFF +  "\n- Chicago\n- New York\n- Washington")
    city_raw = input(" -> Your input: ")
    city = city_raw.lower()

    #dictionary to control the input
    city_str_dict = ["chicago", "new york", "washington"]

    while city not in city_str_dict:
        print("Please enter a valid city:\n-Chicago\n-New York\n-Washington\n")
        city_raw = input(" -> Your input: ")
        city = city_raw.lower()

    print('-' * 40)

    # time filter flow
    print(BOLD + "Which filter do you want to apply:" + ALL_OFF + "\n- none" + ITALIC +
        f" (it shows data for everyday between January and June for the city of {city.title()})" + ITALIC_OFF +
        "\n- month\n- day\n- both" + ITALIC + " (day and month)\n" + ITALIC_OFF)
    chosen_filter_raw = input(" -> Your input: ")
    chosen_filter = chosen_filter_raw.upper()

    #dictionary to control input
    filter_str_dict = ["NONE", "MONTH", "DAY", "BOTH"]
    #dictionary to convert str month to int
    filter_dict = {"NONE": 0, "MONTH": 1, "DAY": 2, "BOTH": 3}

    while chosen_filter not in filter_str_dict:
        print("Please enter a valid filter:\n- none" + "\x1B[3m"
        f" (it shows data for everyday between January and June for the city of {city.title()})" + "\x1B[0m"
        "\n- month\n- day\n- both" + "\x1B[3m" + " (day and month)\n" + "\x1B[0m")
        chosen_filter_raw = input(" -> Your input: ")
        chosen_filter = chosen_filter_raw.upper()

    filter = filter_dict.get(chosen_filter)
    print("This is filter", filter)

    print('-' * 40)

    month = None
    day = None

    #dictionaries to print month and days str
    month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June"}
    day_dict = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

    if filter == 1:
        month = month_filter()
        month_str = month_dict.get(month)
        print(BOLD + f" -> You chose to see the data from {city.title()} filtered by {month_str}" + ALL_OFF)

    elif filter == 2:
        day = day_filter()
        day_str = day_dict.get(day)
        print(BOLD + f" -> You chose to see the data from {city.title()} filtered by {day_str}" + ALL_OFF)

    elif filter == 3:
        month = month_filter()
        day = day_filter()
        month_str = month_dict.get(month)
        day_str = day_dict.get(day)
        print(BOLD + f" -> You chose to to see the data from {city.title()} filtered by {month_str}, and {day_str}" + ALL_OFF)

    else:
        print(BOLD + " -> You chose to see unfiltered data" + ALL_OFF)

    print('-' * 40)

    return city, month, day, filter


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze

        (int) month - number of the month to filter by, or None to apply no month filter
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June"

        (int) day - number of the day of week to filter by, or None to apply no day filter
        0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load city
    if city == "chicago":
        df = pd.read_csv(r"chicago.csv")
    elif city == "new york":
        df = pd.read_csv(r"new_york_city.csv")
    elif city == "washington":
        df = pd.read_csv(r"washington.csv")

    # create month, day and hour columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # applying selected filter(s)
    if day in [0, 1, 2, 3, 4, 5, 6] and month in [1, 2, 3, 4, 5, 6]:
        df = df[df['day'] == day]
        df = df[df['month'] == month]

    elif month in [1, 2, 3, 4, 5, 6]:
        df = df[df['month'] == month]

    elif day in [0, 1, 2, 3, 4, 5, 6]:
        df = df[df['day'] == day]

    df = df.rename(columns={"Unnamed: 0": "Code"})
    df = df.rename(columns={"Trip Duration": "Trip Duration (in seconds)"})

    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel.

        Args
        (DataFrame) -data frame already filtered
        (int) - filter to control which stats to display

    Returns:
        void
    """

    # size of the original data frame without filters vs size of the new filtered data frame

    if pd.isnull(month) and pd.isnull(day):
        print(f"You're seeing the original Data Frame for the city of {city.title()}, with ", load_data(city,None, None).shape[0], "rows")
    else:
        print(f"The original Data Frame for the city of {city.title()} has", load_data(city, None, None).shape[0], "rows")
        print(f"The new Data Frame with the chosen filters has", load_data(city, month, day).shape[0], "rows")
    print('-' * 40)

    print("\n" + BACK_MAGENTA + BOLD + FONT_BLACK + "Calculating The Most Frequent Times of Travel..." + ALL_OFF + "\n")
    start_time = time.time()

    #dictionaries to print time stats in str
    month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June"}
    day_dict = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

    if pd.isnull(month) and pd.isnull(day): # no filters applied - display month, day and hour
        # display the most common month
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        popular_month_mode = df["month"].mode()
        popular_month = popular_month_mode[0]
        popular_month_str = month_dict.get(popular_month)
        print(BOLD + "-The most popular month is: " + ALL_OFF + f"{popular_month_str}")

        # display the most common day of week
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['day'] = df['Start Time'].dt.dayofweek
        popular_day_mode = df["day"].mode()
        popular_day = popular_day_mode[0]
        popular_day_str = day_dict.get(popular_day)
        print(BOLD + "-The most popular day of the week is: " + ALL_OFF + f"{popular_day_str}")

        # display the most common start hour
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['hour'] = df['Start Time'].dt.hour
        popular_hour_mode = df["hour"].mode()
        popular_hour = popular_hour_mode[0]
        print(BOLD + "-The most popular hour is: " + ALL_OFF + f"{popular_hour} Hrs.")

    elif pd.isnull(day):  # filtered by month -display day and hour
        # display the most common day of week
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['day'] = df['Start Time'].dt.dayofweek
        popular_day_mode = df["day"].mode()
        popular_day = popular_day_mode[0]
        popular_day_str = day_dict.get(popular_day)
        print(BOLD + "-The most popular day of the week is: " + ALL_OFF + f"{popular_day_str}")

        # display the most common start hour
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['hour'] = df['Start Time'].dt.hour
        popular_hour_mode = df["hour"].mode()
        popular_hour = popular_hour_mode[0]
        print(BOLD + "-The most popular hour is: " + ALL_OFF + f"{popular_hour} Hrs.")

    elif pd.isnull(month):  # filtered by day - display hour
        # display the most common start hour
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['hour'] = df['Start Time'].dt.hour
        popular_hour_mode = df["hour"].mode()
        popular_hour = popular_hour_mode[0]
        print(BOLD + "-The most popular hour is: " + ALL_OFF + f"{popular_hour} Hrs.")

    else: # filtered by both - display hour
        # display the most common start hour
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['hour'] = df['Start Time'].dt.hour
        popular_hour_mode = df["hour"].mode()
        popular_hour = popular_hour_mode[0]
        print(BOLD + "-The most popular hour is: " + ALL_OFF + f"{popular_hour} Hrs.")

    print(ITALIC + "\nThis operation took %s seconds." % (time.time() - start_time) + ITALIC_OFF)
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args
        (DataFrame) -data frame already filtered

    Returns:
        void
    """

    print("\n" + BACK_MAGENTA + BOLD + FONT_BLACK + "Calculating The Most Popular Stations and Trip..." + ALL_OFF + "\n")
    start_time = time.time()

    # create combination of station column in data frame:
    df["Combination of Stations"] = "Start: " + df["Start Station"] + " / " + "End: " + df["End Station"]

    # mode from every column of the data frame:
    mode_of_each_column = df.mode()
    mode_df = mode_of_each_column.head(1)

    # display most commonly used start station
    start_station_mode = mode_df["Start Station"]
    most_common_start_station = start_station_mode[0]
    print(BOLD + "- The most common start station is: " + ALL_OFF + f"{most_common_start_station}")

    # display most commonly used end station
    end_station_mode = mode_df["End Station"]
    most_common_end_station = end_station_mode[0]
    print(BOLD + "- The most common end station is: " + ALL_OFF + f"{most_common_end_station}")

    # display most frequent combination of start station and end station trip
    combination_mode = df["Combination of Stations"].mode()
    most_common_combination = combination_mode[0]
    print(BOLD + "- The most common combination of stations is: " + ALL_OFF + f"{most_common_combination}")

    print(ITALIC + "\nThis operation took %s seconds." % (time.time() - start_time) + ITALIC_OFF)
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Args
        (DataFrame) -data frame already filtered

    Returns:
        void
    """

    print("\n" + BACK_MAGENTA + BOLD + FONT_BLACK + "Calculating Trip Duration..." + ALL_OFF + "\n")
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration (in seconds)"].sum()
    total_travel_time_seconds = round(total_travel_time, 1)
    total_travel_time_minutes = round(total_travel_time / 3600, 1)
    total_travel_time_days = int(round(total_travel_time_minutes/24, 0))
    print(BOLD + "The total travel time is: " + ALL_OFF + f"{total_travel_time_seconds} seconds, equivalent to "
                f"{total_travel_time_minutes} hours, equivalent to {total_travel_time_days} days.")

    # display mean travel time
    mean_travel_time = df["Trip Duration (in seconds)"].mean()
    mean_travel_time_minutes = round(mean_travel_time / 60, 2)
    print(BOLD + "The average travel time is: " + ALL_OFF + f"{mean_travel_time_minutes} minutes")

    print(ITALIC + "\nThis operation took %s seconds." % (time.time() - start_time) + ITALIC_OFF)
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
     Args
        (DataFrame) -data frame already filtered
        (str) - city to filter stats on gender and birth year

    Returns:
        void
    """

    print("\n" + BACK_MAGENTA + BOLD + FONT_BLACK + "Calculating User Stats..." + ALL_OFF + "\n")
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(BOLD + f"Types and number of users:" + ALL_OFF)
    print("- Subscribers: ", user_types[0])
    print("- Customers: ", user_types[1])
    print(" ")

    if city == "chicago" or city == "new york":
        print(BOLD + "The city of " + FONT_MAGENTA + f"{city.title()}" + ALL_OFF +
              BOLD + " also has statistics for gender, birth year, and age" + ALL_OFF + "\n")

        # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print(BOLD + f"Counts of Gender:" + ALL_OFF)
        print("- Male: ", gender_count[0])
        print("- Female: ", gender_count[1])

        print(ITALIC + FONT_MAGENTA + "*We apologize because our database includes only binary gender values*\n"
              "*We recognize diversity and are working towards making our data more inclusive*" + ALL_OFF)
        print(" ")
        # Display earliest, most recent, and most common year of birth

        # earliest
        birth_min = df["Birth Year"].min()
        earliest_birthyear = int(birth_min)
        print(BOLD + "The earliest year of birth: " + ALL_OFF +  f"{earliest_birthyear}")

        # recent
        birth_max = df["Birth Year"].max()
        recent_birthyear = int(birth_max)
        print(BOLD + "The most recent year of birth: " + ALL_OFF + f"{recent_birthyear}")

        # most common
        birth_mode = df["Birth Year"].mode()
        birthyear_mode_access = birth_mode[0]
        most_common_birthyear = int(birthyear_mode_access)
        print(BOLD + "The most common year of birth: " + ALL_OFF + f"{most_common_birthyear}")
        print(" ")

        # averages of the whole dataframe grouped by gender
        df_modified = df.rename(columns = {"Trip Duration (in seconds)": "Trip Duration (in minutes)"})
        df_modified["Trip Duration (in minutes)"] = df_modified["Trip Duration (in minutes)"] / 60
        averages_by_gender = df_modified.groupby(["Gender"]).mean()

        # average trip in minutes grouped by gender
        average_trips_by_gender = round(averages_by_gender[["Trip Duration (in minutes)"]], 1)
        print(BOLD + "Age and trip averages grouped by gender:" + ALL_OFF + "\n")
        print("The average trip grouped by gender:\n")
        print(average_trips_by_gender)
        print("")

        # average age
        average_birthyear_by_gender = 2021 - averages_by_gender[["Birth Year"]]

        # average age for Female users
        female_avg_age = average_birthyear_by_gender["Birth Year"]["Female"]
        female_avg_age_round = round(female_avg_age)
        print(BOLD + "The average age for Female users is: " + ALL_OFF + f"{female_avg_age_round}")

        # average age for Male users
        male_avg_age = average_birthyear_by_gender["Birth Year"]["Male"]
        male_avg_age_round = round(male_avg_age)
        print(BOLD + "The average age for Male users is: " + ALL_OFF + f"{male_avg_age_round}")

    else:
        print(BOLD + "You chose to see data from Washington city.\n" 
               "The statistics regarding gender, birth year, and age are only available for " + FONT_MAGENTA + "Chicago " + ALL_OFF +
              BOLD + "and " + FONT_MAGENTA + "New York " + ALL_OFF + BOLD + "cities." + ALL_OFF)

    print(ITALIC + "\nThis took %s seconds." % (time.time() - start_time) + ITALIC_OFF)
    print('-' * 40)

def individual_data(df, city):
    """ Cleans the data frame to show individual records.
    Asks the user if he/she wants to see individual records from the filtered data frame.
    If the user does not want to - nothing happens

    Args
        (DataFrame) -data frame already filtered
        (str) - city to filter the individual stats on gender and birth year

    Returns:
        void
    """

    # clean data frame so dataframe does not show columns used for statistics - replacing NaNs with "Not available"
    df_clean = df.drop(["month", "day", "hour", "Combination of Stations"], axis=1)


    #ask for input
    print(BACK_WHITE + FONT_BLACK + BOLD + "Do you want to see individual data? Enter " + BOLD + ITALIC + "yes "
                + ITALIC_OFF + BACK_WHITE + FONT_BLACK + "or " + ITALIC + BOLD + "no." + ALL_OFF + "\n")
    see_data_raw = input(" -> Your input: ")
    see_data = see_data_raw.lower()
    rows_to_show = 0

    #input control
    while True:
        if see_data == "no":
            break

        elif see_data == "yes":
            individual_data = df_clean.iloc[rows_to_show, rows_to_show + 5].copy()
            rows_to_show += 5

            #filter by city because washignton has no gender and birth year
            if city != "washington":

                if pd.isna(individual_data["Gender"]):
                    individual_data["Gender"] = "Not available"

                if individual_data["Birth Year"] and pd.isna(individual_data["Birth Year"]) == False:
                    individual_data["Birth Year"] = round(individual_data["Birth Year"])
                else:
                    individual_data["Birth Year"] = "Not available"

            print(individual_data)
            print('-' * 40)

            print(BOLD + "Do you want to continue exploring individual data?" + ALL_OFF + "\n")
            print("- yes\n- no")
            see_data = input(" -> Your input: ")
            see_data = see_data.lower()

        elif see_data not in ["yes", "no"]:
            print(
                BOLD + "Please write a valid option. Do you want to continue exploring individual data?" + ALL_OFF + "\n")
            print("- yes\n- no")
            see_data = input(" -> Your input: ")
            see_data = see_data.lower()


def main():
    """
    Calls all functions in a loop that can be broken by choosing not to restart the program
    """

    while True:
        
        city, month, day, filter = get_filters()
        df = load_data(city, month, day)
        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        individual_data(df, city)

        # ask for input
        print("\n" + BACK_WHITE + FONT_BLACK + "Would you like to restart the program? Enter " + BOLD + ITALIC + "yes "
              + ITALIC_OFF + BACK_WHITE + FONT_BLACK + "or " + ITALIC + BOLD + "no." + ALL_OFF + "\n")
        restart_raw = input(" -> Your input: ")
        restart = restart_raw.lower()

        # input control
        while restart not in ["yes", "no"]:
            print(BOLD + "Please enter a valid input.")
            print(
                "\n" + BACK_WHITE + FONT_BLACK + "Would you like to restart the program? Enter " + BOLD + ITALIC + "yes "
                + ITALIC_OFF + BACK_WHITE + FONT_BLACK + "or " + ITALIC + BOLD + "no." + ALL_OFF + "\n")
            restart_raw = input(" -> Your input: ")
            restart = restart_raw.lower()

        if restart == "no":
            print(" ")
            print(FONT_CYAN + BOLD + REVERSE + "Thank you for using the US bikesharing data-explorer!" + ALL_OFF)
            print('-' * 40)
            print(FONT_CYAN + UNDERSCORE + "Credits" + ALL_OFF)
            print(
                FONT_CYAN + "The US bikesharing data-explorer was created to fulfil the requirements of the Udacity® Nanodegree Program:\n"
                            "'Programming for Data Science with Python'\n"
                            "Code structure provided by Udacity® - Modifications to the structure and coding by Lina María Pérez González\n"
                            "August 2021 - Siegen, Germany - A corona-quarantine project :)")
            break

if __name__ == "__main__":
    main()
