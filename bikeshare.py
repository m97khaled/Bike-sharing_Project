import numpy as np, pandas as pd, time

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    global city
    global month
    global day
    while True:
        city= str(input("Available cities: Chicago, New York City, Washington\nEnter the desired city to analyze: ")).lower().title()
        if city in ("Chicago", "New York City", "Washington"):
            break
        else:
            city=str(input("\nInvalid input!\nPlease type a city from the available list (Chicago, New York City, Washington): ")).lower().title()
            continue

    #Used to test user's input of month and day.
    test_month=("January", "February", "March", "April", "May", "June")
    test_day=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

    # Month and Day functions used to minimize repition of code.
    # Maintains integrity of user input and avoids script crashing for unexpected invalid inputs.
    def months():
        """
        Filter data to analyze by month according to user's input

        Returns: month
        """
        global month
        while True:
            month = str(input("\nAvailable months: January, February, March, April, May or June.\nPlease enter a month to filter by: ")).lower().title()
            if month in test_month:
                break
            else:
                month= str(input("\nPlease enter a valid month to filter by: ")).lower().title()
                continue
        return (month)

    def days():
        """
        Filter data to analyze by day according to user's input

        Returns: day

        """
        global day
        while True:
            day=str(input("\nPlease enter a day to filter by (Monday - Sunday): ")).lower().title()
            if day in test_day:
                break
            else:
                day= str(input("\nPlease enter a valid day to filter by:")).lower().title()
                continue
        return (day)

    #Filters data according to user's input
    while True:
        sel_filter= str(input("\nWould you like to filter the data based on:\nMonth, day, both or without a filter (type 'all' to display all data)?\nFilter by:")).title()
        if sel_filter in ("Month", "Day", "Both", "All"):
            break
        else:
            sel_filter=str(input("\nInvalid input! Please type a valid filter option:\n")).lower().title()
            continue

    if sel_filter == "Month":
        months()
        day="All"

    elif sel_filter == "Day":
        days()
        month="All"

    elif sel_filter == "Both":
        months()
        days()

    elif sel_filter =="All":
        month,day="All","All"

    print('-'*40)
    return (city, month, day)

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    global df
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'All':
        # filter by month to create the new dataframe
        df = df[df['Month']==month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['Day of Week']==day.lower().title()]
    return (df)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour
    print("Most common month: ",df['Month'].mode()[0])
    print("Most common day of week: ",df['Day of Week'].mode()[0])
    print("Most common start hour: ",df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip
    print("Most commonly used start station: ",df['Start Station'].mode()[0])
    print("Most commonly used end station: ",df['End Station'].mode()[0])
    print("Most frequent trip: From", (df['Start Station'] + " Station to " + df['End Station'] + " Station").mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time
    df['End Time'] = pd.to_datetime(df['End Time'])

    print("Total travel time: ", (df['End Time'] - df['Start Time']).sum())
    print("Average travel time: ",(df['End Time'] - df['Start Time']).mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth
    print(df['User Type'].value_counts().to_frame(" "))

    if 'Gender' not in df:
        print("No gender data available for this city")
    else:
        print(df['Gender'].value_counts().to_frame(" "))
    if 'Birth Year' not in df:
        print("No age data available for this city")
    else:
        print("Oldest Birth Year: ", int(df['Birth Year'].min()),"\nYoungest Birth Year: ", int(df['Birth Year'].max()), "\nMost common birth year: ", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    while True:
        sample = str(input("Would you like to view random raw data? (Yes or No).")).lower().title()
        if sample == "Yes":
            print(df.sample(n = 5))
            continue
        elif sample == "No":
            break
        else:
            print("\nInvalid input!")
            continue
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().title()
        if restart != 'Yes':
            break


if __name__ == "__main__":
    main()