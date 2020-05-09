import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Choose one city (chicago, new york city or washington): ")
    while city not in ("chicago","new york city","washington"):
        city=input("Choose one city (chicago, new york city or washington): ")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Choose one month (all, january,february...,june): ")
    while month not in ("all","january","february","march","april","may","june"):
        month=input("Choose one month (all, january,february...,june): ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Choose one day (all, monday,...,sunday): ")
    while day not in ("all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"):
        day=input("Choose one day (all, monday,...,sunday): ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    print(df)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month is "+str(popular_month))
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day is "+str(popular_day))

    # TO DO: display the most common start hour
    popular_start_hour = df['Start Time'].mode()[0]
    print("The most common start hour is "+str(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station  = df['Start Station'].mode()[0]
    print("The most common start station is "+str(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station  = df['End Station'].mode()[0]
    print("The most common end station is "+str(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("Total travel time: "+str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("Mean travel time: "+str(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print("Counts of user types: "+str(user_types))

    # TO DO: Display counts of gender
    gender_types=df['Gender'].value_counts()
    print("Counts of gender: "+str(gender_types))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year=df['Birth Year'].min()
    recent_year=df['Birth Year'].max()
    common_year=df['Birth Year'].mode()[0]
    print("The earliest year of birth is "+str(earliest_year))
    print("The most recent year of birth is "+str(recent_year))
    print("The most common year of birth is "+str(common_year))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
